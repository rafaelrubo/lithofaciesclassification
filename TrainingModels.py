# This block of code should be preceded by loading data, as shown in GeometricAugmentations.py

# Importing libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras.optimizers
from keras.optimizers import SGD
import pandas as pd

# Defining CNN architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(256,256,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(6))
model.add(Activation('softmax'))

# Establishing parameters and compiling the model
opt = SGD(lr=0.001)
model.compile(loss = 'categorical_crossentropy', optimizer = opt, metrics=['accuracy'])

#Training the model
history = model.fit(train_generator,
                    steps_per_epoch=train_generator.n//train_generator.batch_size,
                    validation_data=validation_generator,
                    validation_steps=validation_generator.n//validation_generator.batch_size,
                    epochs=300)

#Predicting test data
Y_pred = model.predict_generator(test_generator, steps = test_generator.n//test_generator.batch_size + 1, verbose=1)

#Creating test results dataframe
y_pred=np.argmax(Y_pred,axis=1)
labels = (test_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in y_pred]
res = pd.DataFrame(predictions)

#Creating filenames dataframe
filenames=test_generator.filenames
files = pd.DataFrame(filenames)

#Exporting test results to a csv file
final = pd.concat([files, res], axis=1)
final.to_csv("results.csv")