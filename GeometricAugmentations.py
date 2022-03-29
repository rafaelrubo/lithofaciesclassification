# Importing libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

# Progressively loading images from directory
# Creating generator for geometric augmentations

# Training data
TRAINING_DIR = "./train/"
training_datagen = ImageDataGenerator(
      rescale = 1./255,
      rotation_range=36,
      width_shift_range=0.3,
      height_shift_range=0.3,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      vertical_flip=True,
      brightness_range=[0.6,1.0],
      fill_mode='reflect')

# Validation data
VALIDATION_DIR = "./valid/"
validation_datagen = ImageDataGenerator(
      rescale = 1./255)

# Test data
TEST_DIR = "./test/"
test_datagen = ImageDataGenerator(
      rescale = 1./255)

# Preparing iterators for training data
train_generator = training_datagen.flow_from_directory(
    TRAINING_DIR,
    batch_size=6,
    target_size=(256,256),
    class_mode='categorical',
    shuffle=False)

# Preparing iterators for validation data
validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    batch_size=6,
    target_size=(256,256),
    class_mode='categorical',
    shuffle=False)

# Preparing iterators for test data
test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    batch_size=6,
    target_size=(256,256),
    class_mode='categorical',
    shuffle=False)