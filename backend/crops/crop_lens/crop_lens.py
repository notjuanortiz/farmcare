#import cv2 as cv 
from glob import glob
import matplotlib.pyplot as plt 
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ["SM_FRAMEWORK"] = "tf.keras"
# from tensorflow.python.ops.gen_batch_ops import batch
# from tensorflow.python.ops.math_ops import truediv 
os.environ['TFF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow import keras
import numpy as np 
import PIL 
import tensorflow as tf
from tensorflow import keras 
# from tensorflow.keras.layers import Normalization
# from tensorflow.keras.layers import CenterCrop
# from tensorflow.keras.layers import Rescaling
# tfds.disable_progress_bar()
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
import pathlib
import autokeras as ak

# upload_image() -> retrieve user image from Google Cloud 

filename = '/Users/hijabsyeda/FarmCare_APP/farmcare/backend/crop_lens/tomato.jpeg'

# establish a base size for all image files passed to network 
def rescale_image(image):
    plt.imshow(image), plt.title("Original")
    plt.xticks([]), plt.yticks([])
    plt.show()
    new_height = 220 
    new_width = 220 
    new_dimensions = (new_height, new_width)
    result = cv.resize(image, new_dimensions, interpolation = cv.INTER_LINEAR)
    print("New Image Dimensions = ", result.shape[0], result.shape[1])
    plt.imshow(result), plt.title("Resized Image")
    plt.xticks([]), plt.yticks([])
    plt.show()
    # Remove noise -> Gaussian Blur
    blur = cv.GaussianBlur(result, (5,5), 0)
    image = blur
    plt.imshow(image), plt.title("Gaussian Blur applied to Image")
    plt.xticks([]), plt.yticks([])
    plt.show()
    # Segmentation
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    # Displaying segmented images
    plt.imshow(thresh), plt.title("Segmented Image")
    plt.xticks([]), plt.yticks([])
    plt.show()
    # Sharpen the image 
    kernel = np.ones((3,3), np.uint8)
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations = 2)
    sure_background = cv.dilate(opening, kernel, iterations = 3)
    # Finding sure foregound area
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    ret, sure_foreground = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    # Finding unknown region 
    sure_foreground = np.uint8(sure_foreground)
    unknown = cv.subtract(sure_background, sure_foreground)
    #displaying segmented back ground 
    plt.imshow(sure_background), plt.title("Segmented Background")
    plt.xticks([]), plt.yticks([])
    plt.show()
    # Seperate diffrent objects with markers
    ret, markers = cv.connectedComponents(sure_foreground)
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(image, markers)
    image[markers == -1] = [255,0,0]
    plt.imshow(markers), plt.title("Marked Image")
    plt.xticks([]), plt.yticks([])
    plt.show()


def load_image():
    image = cv.imread(filename, cv.IMREAD_UNCHANGED)

    if image is None: 
        sys.exit("Could not read the image")

    validate_image_size(image)
    # plt.imshow(img, cmap='gray')
    
    cv.imshow("Original Image", image)
    k = cv.waitKey(0)
    cv.destroyAllWindows() 
    rescale_image(image)

# Check whether the image dimensions do not exceed 3648 x 2736 (10 megapixels) or less than 720 x 480 (NTSC with 4:3 aspect ratio)
def validate_image_size(image):
    height = image.shape[0]
    width = image.shape[1]
    print("Image Dimensions ", height, width)
    try: 
        is_height_between = height in range(720,3648)
        is_width_between = width in range(2736, 480)
        if(is_height_between and is_width_between):
            print("Image size is supported")
    except: 
        sys.exit("Invalid image size. Image size is too big (greater than 10 megapixels) or is too small (less than 4:3 aspect ratio")



# Check should be able to validate an incorect extension image file, curropted file. and an invalid image file 
def validate_image_format():

    print("Check #1: check whether the file is not available or is curropted")
    image = cv.imread(filename)
    try: 
        dimensions = image.shape
        print(dimensions)
        print("Check #1 Success: File contains height, width, and channel")
    except:
        sys.exit("[INFO] Image is not available or is curropted")

    print("Check #2: check whether the file is a valid image file")
    try: 
        img = PIL.Image.open(filename)
        img.verify()
        print("Check #2 Success: PIL was able to read and identify that file is a valid image file")
    except IOError: 
        print("File is not a valid image file")
    except: 
        sys.exit("file is broken")

    print("Check #3: checking whether image file has suitable format ...jpeg, ...jpg, or ...png")
    print(img.format)
    if(img.format.lower() in ['png', 'jpg', 'jpeg']):
        print("Success. File format accepted, Image validated...")
        load_image()
    else:
        sys.exit("File is not broken, is an image file, but is not a .png, .jpg, or .jpeg")



# validate_image_format()

def train_data():
    # since my data fits into memory, the dataset will be as a numpy array 
    # DATA_URL = './archive2'
    # crop_path = tf.keras.utils.get_file('backend/crop_lens/archive 2/crop_images', DATA_URL)
    # with np.load(crop_path) as data: 
    #     train_examples = data['x_train']
    #     train_labels = data['y_train']
    #     test_examples = data['x_test']
    #     test_labels = data['y_test']

    # train_dataset = tf.data.Dataset.from_tensor_slices((train_examples, train_labels))
    # test_dataset = tf.data.Dataset.from_tensor_slices((test_examples, test_labels))

    # BATCH_SIZE = 64
    # SHUFFLE_BUFFER_SIZE = 100

    # train_dataset = train_dataset.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
    # test_Dataset = test_dataset.batch(BATCH_SIZE)

    # # build and train model 
    # model = tf.keras.Sequential([
    #     tf.keras.layers.Flatten(input_shape=(28,28)),
    #     tf.keras.layers.Dense(128, activation='relu'),
    #     tf.keras.layers.Dense(10)
    # ])

    # model.compile(optimizer=tf.keras.optimizers.RMSprop(), 
    #             loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    #             metrics = ['sparse_categorical_accuracy'])

    # model.fit(train_dataset, epochs =10)
    # crop_dir = pathlib.Path('./agriculture_dataset/crop_images')
    # image_count = len(list(crop_dir.glob('*/*.jpeg')))
    # print("Number of images in dataset:", image_count)

    # # rice = list(crop_dir.glob('rice/*.jpeg')) # does not sort the images 
    # # PIL.Image.open(str(rice[0])) # does not show the image even though it exists 

    # # parameters for the dataset
    # batch_size = 32
    # img_height = 180 
    # img_width = 180
    # # create a dataset 
    # train_ds = tf.keras.utils.image_dataset_from_directory(
    #     crop_dir, 
    #     validation_split=0.2,
    #     subset="training",
    #     seed=123,
    #     image_size=(img_height, img_width),
    #     batch_size=batch_size)
    # print(train_ds)

    # val_ds = tf.keras.utils.image_dataset_from_directory(
    #     crop_dir, 
    #     validation_split = 0.2,
    #     subset="validation",
    #     seed=123,
    #     image_size=(img_height, img_width),
    #     batch_size=batch_size)
    # print(val_ds)

    # class_names = train_ds.class_names
    # plt.figure(figsize=(10,10))
    # for images, labels in train_ds.take(1):
    #     for i in range(9):
    #         ax = plt.subplot(3,3, i + 1)
    #         plt.imshow(images[i].numpy().astype("uint8"))
    #         plt.title(class_names[labels[i]])
    #         plt.axis("off")
    
    # for image_batch, labels_batch in train_ds
    #     print(image_batch.shape)
    #     print(labels_batch.shape)
    #     break

    # # standarize RGB data 0-255 -> 0,1
    # normalization_layer = tf.keras.layers.Rescaling(1./255)
    # normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    # image_batch, labels_batch = next(iter(normalized_ds))
    # first_image = image_batch[0]
    # # Notice the pixel values are now in `[0,1]`
    # print(np.min(first_image), np.max(first_image))

    # AUTOTUNE = tf.data.AUTOTUNE

    # # dataset.cache keeps images in memory after they are loaded off disk 
    # train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    # val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    # # train a model 
    # num_classes =  5
    # model = tf.keras.Sequential([
    #     tf.keras.layers.Rescaling(1./255),
    #     tf.keras.layers.Conv2D(32, 3, activation='relu'),
    #     tf.keras.layers.MaxPooling2D(),
    #     tf.keras.layers.Conv2D(32, 3, activation='relu'),
    #     tf.keras.layers.MaxPooling2D(),
    #     tf.keras.layers.Conv2D(32, 3, activation='relu'),
    #     tf.keras.layers.MaxPooling2D(),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation='relu'),
    #     tf.keras.layers.Dense(num_classes)
    # ])

    # model.compile(
    #     optimizer='adam',
    #     loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
    #     metrics=['accuracy'])

    # model.fit(
    #     train_ds,
    #     validation_data=val_ds,
    #     epochs=3
    # )

    # START 
    # since plant_village only provides the train data set we need to split the test and train dataset 
    # def get_dataset_partition_tf(ds, ds_size, train_split = 0.8, test_split = 0.2, shuffle=False, shuffle_size=10000):
    #     assert (train_split + test_split) == 1
    #     if shuffle:
    #         ds = ds.shuffle(shuffle_size, seed = 12)

    #     train_size = int(train_split * ds_size)

    #     train_ds = ds.take(train_size)
    #     test_ds = ds.skip(train_size)

    #     return train_ds, test_ds 

    # builder = tfds.builder('plant_village')
    # info = builder.info
   
    # ds = tfds.load(
    #     name ='plant_village',
    #     split = 'train',
    #     shuffle_files = True
    # ) 
    # ds_size = len(ds)
    # train_ds, test_ds = get_dataset_partition_tf(ds, ds_size)
    # print(train_ds)
    # print(test_ds)
    
    # # show examples 
    # # fig = tfds.show_examples(train_ds, info)
    # # fig2 = tfds.show_examples(test_ds, info)
    
    # # additional data processing before passing to network  
    # train_images = np.array([example['image'].numpy()[:,:,0] for example in train_ds])
    # train_labels = np.array([example['label'].numpy()  for example in train_ds])

    # test_images = np.array([example['image'].numpy()[:,:,0]  for example in test_ds])
    # test_labels = np.array([example['label'].numpy()  for example in test_ds])
    

    # # train_images = train_images.reshape(43442, 256, 256, 1)
    # # test_images = test_images.reshape(10861, 256, 256, 1)
    # # # normalize from uint8 -> float32
    # # train_images = train_images.astype('float32') / 255.0 
    # # test_images = test_images.astype('float32') / 255.0

    # # print("Starting training...")
    # # # train the network 
    # # # model = keras.Sequential([
    # # #     keras.layers.Flatten(),
    # # #     keras.layers.Dense(512, activation='relu', name='first_layer'),
    # # #     keras.layers.Dense(256, name='second_layer', activation='relu'),
    # # #     keras.layers.Dense(38, activation='softmax')
    # # # ])
    # # # model.compile(
    # # #     optimizer='adam',
    # # #     loss = keras.losses.SparseCategoricalCrossentropy(),
    # # #     metrics = ['accuracy']
    # # # )
    # # # model.fit(train_images, train_labels, epochs=5, batch_size=32)
    # # # # for unseen data 
    # # # model.evaluate(test_images, test_labels)

    # # # train as a convolutional network 
    # # model = keras.Sequential([
    # #     keras.layers.Conv2D(64, 3, activation='relu', input_shape=(256,256,1)),
    # #     keras.layers.Conv2D(32, 3, activation='relu'),
    # #     keras.layers.Flatten(),
    # #     keras.layers.Dense(3, activation='softmax')
    # # ])
    # # model.compile(
    # #     optimizer='adam',
    # #     loss = keras.losses.SparseCategoricalCrossentropy(),
    # #     metrics = ['accuracy']
    # # )
    # # model.fit(train_images, train_labels, epochs=5, batch_size=32)
    # # model.evaluate(test_images, test_labels)

    ###### 
    image_ds = tf.data.Dataset.list_files('./plant-seedlings-classification/train/*/*.png', shuffle=True)

    class_names = ['Black Grass', 'Charlock', 'Cleavers','Common Chickweed', 'Common Wheat', 'Fat Hen','Loose Silky-bent', 'Maize', 'Scentless Mayweed', 'Sheperds-flowered Cranesbill', 'Sugar beet']
    image_count = len(image_ds)
    print(image_count)
    
    batch_size = 32
    img_height = 180
    img_width = 180
    
    crop_path = './plant-seedlings-classification/train/'
    train_data = ak.image_dataset_from_directory(
        crop_path,
        validation_split = 0.2,
        subset = 'training',
        seed = 123,
        image_size = (img_height, img_width),
        batch_size = batch_size,
    )

    test_data = ak.image_dataset_from_directory(
        crop_path,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )

    clf = ak.ImageClassifier(overwrite=True, max_trials=1)
    clf.fit(train_data, epochs=2)
    print(clf.evaluate(test_data))

    # model = clf.export_model()

    # try: 
    #     model.save("model_autokeras", save_format="tf")
    # except Exception:
    #     model.save("model_autokeras.h5")

    # loaded_model = load_model("model_autokeras", custom_objects=ak.CUSTOM_OBJECTS)
    # predicted_y = loaded_model.predict(tf.expand_dims(test_data, -1))
    # print(predicted_y)
    # predicted_y = clf.predict(test_data)
    # print(predicted_y)

    # from keras  
    # dataset = keras.preprocessing.image_dataset_from_directory(
    #     './plant-seedlings-classification/train/',
    #     batch_size = 64,
    #     image_size = (200,200)
    # )

    # train_data = np.random.randint(0,256, size= (64,200,200,3)).astype("float32")

    # normalizer = Normalization(axis=-1)
    # normalizer.adapt(train_data)

    # normalized_data = normalizer(train_data)

    # cropper = CenterCrop(height=150, width=150)
    # scaler = Rescaling(scale=1.0 / 255)
    # output_data = scaler(cropper(train_data))

    # inputs = keras.Input(shape=(150,150,3))
    # x = CenterCrop(height=150,width=150) (inputs)
    # x = Rescaling(scale=1.0/255)(x)

    # x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu")(x)
    # x = layers.MaxPooling2D(pool_size=(3, 3))(x)
    # x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu")(x)
    # x = layers.MaxPooling2D(pool_size=(3, 3))(x)
    # x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu")(x)

    # x = layers.GlobalAveragePooling2D()(x)

    # num_classes = 10
    # outputs = layers.Dense(num_classes, activation="softmax")(x)

    # model = keras.Model(input = inputs, output = outputs)

    # data = np.random.randint(0, 256, size=(64, 200, 200, 3)).astype("float32")
    # processed_data = model(data)
    # print(processed_data.shape)

    # model.sumary()
    # data_dir = './plant-seedlings-classification/'
    # class_names = ['Black Grass', 'Charlock', 'Cleavers','Common Chickweed', 'Common Wheat', 'Fat Hen','Loose Silky-bent', 'Maize', 'Scentless Mayweed', 'Sheperds-flowered Cranesbill', 'Sugar beet']

    # train_ds = tf.data.Dataset.list_files('./plant-seedlings-classification/train', shuffle=True)
    # test_ds  = tf.data.Dataset.list_files('./plant-seedlings-classification/test', shuffle=True)
    # for file in image_ds.take(5):
    #     print(file.numpy())

    # train_size = len(train_ds)
    # test_size  = len(test_ds)

    # print(train_size)
    # print(test_size)


train_data()