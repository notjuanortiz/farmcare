import os
from PIL.Image import Image
import numpy as np
from numpy.random.mtrand import f 
import tensorflow as tf 
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.models import Sequential, save_model, load_model

train_ds = tf.keras.utils.image_dataset_from_directory(
    './plant_village/',
    batch_size = 32,
    image_size = (128,128),
    shuffle = True,
    label_mode = 'categorical',
    color_mode = 'grayscale', 
    seed = 123,
    validation_split = 0.8,
    subset = 'training'
)
test_ds = tf.keras.utils.image_dataset_from_directory(
    './plant_village/',
    batch_size = 32,
    image_size = (128,128),
    shuffle = True,
    label_mode = 'categorical',
    color_mode = 'grayscale', 
    seed = 123,
    validation_split = 0.2,
    subset = 'validation'
)

print(train_ds)
print(test_ds)

train_ds = train_ds.prefetch(buffer_size = 32)
test_ds  = test_ds.prefetch(buffer_size = 32)

data_augmentation = keras.Sequential(
    [
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.1),
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


model = make_model(input_shape=(128,128) + (1,), num_classes=16)
# keras.utils.plot_model(model, show_shapes=True)

epochs = 5

# callbacks = [
#     keras.callbacks.ModelCheckpoint("model.{epoch:02d}-{accuracy:.2f}.h5"),
# ]
model.compile(
    optimizer=keras.optimizers.Adam(1e-3),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)
model.fit(
    train_ds, epochs=epochs, validation_data=train_ds, batch_size = 32,
)

saved_model_file_path = './.saved_model'
save_model(model, saved_model_file_path)

# load the model 
model = load_model(saved_model_file_path, compile = True)

# for user input image 
img = keras.preprocessing.image.load_img(
    "./plant_village/Grape___Black_rot/0a06c482-c94a-44d8-a895-be6fe17b8c06___FAM_B.Rot_5019.JPG", color_mode = 'grayscale', target_size=(128,128,1), interpolation = 'nearest'
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) 
print(img_array.shape)
predictions = model.predict(img_array)
score = predictions[0]
# print(
#     "Image is %.2f "
#     % (100 * (1 - score), 100 * score)
# )
print(predictions)

classes = np.argmax(predictions, axis = 1)
print(classes)
