from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
# import glob
# import imageio
# import matplotlib.pyplot as plt
# import numpy as np
# import os
# import PIL
# from tensorflow.keras import layers
# import time
# from IPython import display
TF_CPP_MIN_LOG_LEVEL=2

(train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')
train_images = (train_images - 127.5) / 127.5 # Normalize the images to [-1, 1]

print(type(train_images))
print(train_images.shape)












































