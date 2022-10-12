import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from tensorflow import keras
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import RMSprop

train = ImageDataGenerator(rescale=1/255)
val = ImageDataGenerator(rescale=1/255)

train_data = train.flow_from_directory('/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/train', batch_size=32,class_mode='categorical')
val_data = val.flow_from_directory('/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/val')
print(cv2.imread('/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/train/ThumbsDown/img0.png').shape)