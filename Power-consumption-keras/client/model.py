
import json
import os

import numpy as np
import tensorflow as tf


from fedn.utils.helpers.helpers import get_helper, save_metadata, save_metrics

HELPER_MODULE = 'numpyhelper'
helper = get_helper(HELPER_MODULE)


def compile_model(img_rows=28, img_cols=28):
    # Set input shape
    #input_shape = (img_rows, img_cols, 1)

    # Define model
    opt = tf.keras.optimizers.SGD(lr=0.0001)
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(64, input_dim=4, activation="relu"))
    model.add(tf.keras.layers.Dense(32, activation="relu"))
    model.add(tf.keras.layers.Dense(1, activation="linear"))
    #model.summary()
    model.compile(loss = "mse", optimizer = opt,metrics=['mae'])

    return model

def init_seed(out_path='seed.npz'):

    weights = compile_model().get_weights()
    helper.save(weights, out_path)

if __name__ == "__main__":
    init_seed('../seed.npz')
