import os
from os import listdir
import cv2 as cv
import numpy as np
import pickle 
import tensorflow as tf 
from tensorflow import keras
from keras.preprocessing.image import img_to_array

from tensorflow.keras.models import save_model, load_model
from numpy.random import seed
import random

seed(random.randint(1,10000))

default_image_size = (128,128)
height = 128
width = 128
directory_root = './plant_village'
croplens_directory = os.path.abspath('./backend/crops/crop_lens')

def convert_image_to_array(image):
    try: 
        # image = plt.imread(image)
        image = cv.imread(image)
        if image is not None: 
            image = cv.resize(image, default_image_size)
            return img_to_array(image)
        else:
            return img_to_array(image)
    except Exception as e:
        print("Error converting image")
        return None 

def extract_features():
    image_list, label_list = [], []

    try:
        print("[INFO] Loading images inside dataset...")
        root_dir = listdir(directory_root)
        for directory in root_dir :
            # remove .DS_Store from list
            if directory == ".DS_Store" :
                root_dir.remove(directory)
                print("remove")

        for plant_folder in root_dir :
            plant_disease_folder_list = listdir(f"{directory_root}/{plant_folder}")
            print("[INFO] Processing images inside of class {}...".format(plant_folder))

            for image_file in plant_disease_folder_list:
                image_dir = directory_root + "/" + plant_folder + "/" + image_file
                new_name = image_file.replace(" ", "_")
                new_image_dir = directory_root + "/" + plant_folder + "/" + new_name
                os.replace(image_dir, new_image_dir)

                if new_image_dir.endswith(".jpg") == True or new_image_dir.endswith(".JPG") == True or new_image_dir.endswith(".png") == True:
                    image_list.append(convert_image_to_array(new_image_dir))
                    label_list.append(plant_folder)

        print("[INFO] Image loading completed")  
    except Exception as e:
        print(f"Error : {e}")


    return label_list

def train_again():

    train_ds = tf.keras.utils.image_dataset_from_directory(
        './plant_village',
        batch_size = 32,
        image_size = (128,128),
        shuffle = False, 
        color_mode = 'grayscale', 
        seed = 123,
        validation_split = 0.7,
        subset = 'training'
    )
    test_ds = tf.keras.utils.image_dataset_from_directory(
        './plant_village',
        batch_size = 32,
        image_size = (128,128),
        shuffle = False,
        color_mode = 'grayscale', 
        seed = 123,
        validation_split = 0.3,
        subset = 'validation'
    )

    class_len = len(train_ds.class_names)

    # for dataset to be loaded to buffer from memory
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

    # to prevent overfitting 
    data_augmentation = keras.Sequential(
        [
            tf.keras.layers.RandomFlip("horizontal", input_shape = (height, width, 1)),
            tf.keras.layers.RandomRotation(0.1),
            tf.keras.layers.RandomZoom(0.1)
        ]
    )

    def make_model(input_shape, num_classes):
        inputs = keras.Input(shape=input_shape)
        # Image augmentation block
        x = data_augmentation(inputs)

        # Entry block
        x = tf.keras.layers.Rescaling(1.0 / 255)(x)
        x = tf.keras.layers.Conv2D(32, 3, strides=2, padding="same")(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Activation("relu")(x)

        x = tf.keras.layers.Conv2D(64, 3, padding="same")(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Activation("relu")(x)

        previous_block_activation = x  
        # print(model.summary())

        for size in [128, 256, 512, 728]:
            x = tf.keras.layers.Activation("relu")(x)
            x = tf.keras.layers.SeparableConv2D(size, 3, padding="same")(x)
            x = tf.keras.layers.BatchNormalization()(x)

            x = tf.keras.layers.Activation("relu")(x)
            x = tf.keras.layers.SeparableConv2D(size, 3, padding="same")(x)
            x = tf.keras.layers.BatchNormalization()(x)

            x = tf.keras.layers.MaxPooling2D(3, strides=2, padding="same")(x)

            # Project residual
            residual = tf.keras.layers.Conv2D(size, 1, strides=2, padding="same")(
                previous_block_activation
            )
            x = tf.keras.layers.add([x, residual])  
            previous_block_activation = x  
            # print(model.summary())

        x = tf.keras.layers.SeparableConv2D(1024, 3, padding="same")(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Activation("relu")(x)

        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        x = tf.keras.layers.Dropout(0.5)(x)
        outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)

        return keras.Model(inputs, outputs)


    model = make_model(input_shape=(128,128) + (1,), num_classes = class_len)
    # keras.utils.plot_model(model, show_shapes=True)
    model.summary()

    epochs = 10

    callbacks = [
        keras.callbacks.ModelCheckpoint("model.{epoch:02d}-{accuracy:.2f}.h5"),
    ]

    model.compile(
        optimizer = keras.optimizers.Adam(1e-3),
        loss = "sparse_categorical_crossentropy",
        metrics = ["accuracy"],
    )

    model.fit(
        train_ds, 
        epochs = epochs, 
        validation_data = train_ds, 
        batch_size = 32,
    )

    saved_model_file_path = './saved_model'
    save_model(model, saved_model_file_path)

    return model 

def load_image(link):
    import requests
    import shutil
    import os
    
    _, ext = os.path.splitext(link)
    
    r = requests.get(link, stream=True)
    with open('temp.' + ext, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        
    img = keras.preprocessing.image.load_img('temp.' + ext, color_mode = 'grayscale', 
        target_size = (128, 128, 1), 
        interpolation = 'nearest')
    return keras.preprocessing.image.img_to_array(img)

def crop_lens(imagepath):
    '''
    Returns predicted crop name
    '''
    label_list = ['Apple__Apple_scab', 'Apple__Black_rot', 'Apple__Cedar_apple_rust', 'Apple__healthy', 'Blueberry__healthy', 'Cherry_(including_sour)__healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Orange___Haunglongbing_(Citrus_greening)']

    # to train model again 
    # model = train_again()
    model = load_model(croplens_directory + '/saved_model')
    # # there is a checkpoint warning, -> because we are only using the model on testing data so we can ignore the warning 
    # checkpoint = tf.train.Checkpoint(model)
    # save_path = checkpoint.save('./tmp/training_checkpoints')    
    # checkpoint.restore(save_path).assert_consumed()
    # evaluate restored model 

    img = load_image('https://i.ibb.co/C7L0c5c/apple-leaf.jpg')


    print(img.shape)

    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) 
    # loss, acc = model.evaluate(img_array)
    # print('Restored model, accuracy: {:5.2f}%'.format(100 * acc))

    print(model.predict(img_array).shape)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    # can extract label list from extract_features()
    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(label_list[np.argmax(score)], 100 * np.max(score))
    )
    return label_list[np.argmax(score)]

# extract_features()
crop_name = crop_lens("testimage.png")
print(crop_name)