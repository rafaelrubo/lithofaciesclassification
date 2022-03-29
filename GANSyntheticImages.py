# Importing libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Reshape
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import LeakyReLU, Dropout
from keras.layers import BatchNormalization
from keras.optimizers import Adam, RMSprop

# Progressively loading images from directory
# Creating generator

GAN_DIR = "./gan/"
gan_datagen = ImageDataGenerator(
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

# Preparing iterators
gan_generator = gan_datagen.flow_from_directory(
    GAN_DIR,
    batch_size=6,
    target_size=(256,256),
    class_mode='categorical',
    shuffle=False)

# confirm the iterator works
batchX, batchy = gan_generator.next()
batchX = batchX.reshape(-1, 64, 64, 3).astype(np.float32)

# Defining the discriminator model
def discriminator():
    net = Sequential()
    input_shape = (64, 64, 3)
    dropout_prob = 0.4
    net.add(Conv2D(64, 5, strides=2, input_shape=input_shape, padding='same'))
    net.add(LeakyReLU())
    net.add(Conv2D(128, 5, strides=2, padding='same'))
    net.add(LeakyReLU())
    net.add(Dropout(dropout_prob))
    net.add(Conv2D(256, 5, strides=2, padding='same'))
    net.add(LeakyReLU())
    net.add(Dropout(dropout_prob))
    net.add(Conv2D(512, 5, strides=2, padding='same'))
    net.add(LeakyReLU())
    net.add(Dropout(dropout_prob))
    net.add(Flatten())
    net.add(Dense(1))
    net.add(Activation('sigmoid'))
    return net

# Defining the generator model
def generator():
    net = Sequential()
    dropout_prob = 0.4
    net.add(Dense(8*8*256, input_dim=100))
    net.add(BatchNormalization(momentum=0.9))
    net.add(Activation('relu'))
    net.add(Reshape((8,8,256)))
    net.add(Dropout(dropout_prob))
    net.add(UpSampling2D())
    net.add(Conv2D(128, 5, padding='same'))
    net.add(BatchNormalization(momentum=0.9))
    net.add(Activation('relu'))
    net.add(UpSampling2D())
    net.add(Conv2D(128, 5, padding='same'))
    net.add(BatchNormalization(momentum=0.9))
    net.add(Activation('relu'))
    net.add(UpSampling2D())
    net.add(Conv2D(64, 5, padding='same'))
    net.add(BatchNormalization(momentum=0.9))
    net.add(Activation('relu'))
    net.add(Conv2D(32, 5, padding='same'))
    net.add(BatchNormalization(momentum=0.9))
    net.add(Activation('relu'))
    net.add(Conv2D(3, 5, padding='same'))
    net.add(Activation('sigmoid'))
    return net

# Establishing parameters and compiling models
optim_discriminator = RMSprop(lr=0.0002, clipvalue=1.0, decay=6e-8)
model_discriminator = Sequential()
model_discriminator.add(net_discriminator)
model_discriminator.compile(loss='binary_crossentropy', optimizer=optim_discriminator, metrics=['accuracy'])
optim_adversarial = Adam(lr=0.0001, clipvalue=1.0, decay=3e-8)
model_adversarial = Sequential()
model_adversarial.add(net_generator)

# Disable layers in discriminator
for layer in net_discriminator.layers:
    layer.trainable = False
model_adversarial.add(net_discriminator)
model_adversarial.compile(loss='binary_crossentropy', optimizer=optim_adversarial, metrics=['accuracy'])

# Training the models
batch_size = 10
for i in range(0, 20001):
    images_train = batchX
    noise = np.random.uniform(-1.0, 1.0, size=[batch_size, 100])
    images_fake = net_generator.predict(noise)
    x = np.concatenate((images_train, images_fake))
    y = np.ones([2*batch_size, 1])
    y[batch_size:, :] = 0 
    # Train discriminator for one batch
    d_stats = model_discriminator.train_on_batch(x, y)
    y = np.ones([batch_size, 1])
    # Train the generator for a number of times
    noise = np.random.uniform(-1.0, 1.0, size=[batch_size, 100])
    a_stats = model_adversarial.train_on_batch(noise, y)