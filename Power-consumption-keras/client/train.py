import json
import os
import sys
import fire
import numpy as np
import tensorflow as tf

from data import load_data
from model import compile_model

from fedn.utils.helpers.helpers import get_helper, save_metadata, save_metrics

HELPER_MODULE = 'numpyhelper'
helper = get_helper(HELPER_MODULE)

def train(in_model_path, out_model_path, data_path=None, batch_size=32, epochs=1):
    """ Complete a model update.

    Load model paramters from in_model_path (managed by the FEDn client),
    perform a model update, and write updated paramters
    to out_model_path (picked up by the FEDn client).

    :param in_model_path: The path to the input model.
    :type in_model_path: str
    :param out_model_path: The path to save the output model to.
    :type out_model_path: str
    :param data_path: The path to the data file.
    :type data_path: str
    :param batch_size: The batch size to use.
    :type batch_size: int
    :param epochs: The number of epochs to train.
    :type epochs: int
    """
    # Load data
    x_train, y_train = load_data(data_path)

    # Load model
    model = compile_model()
    #weights = load_parameters(in_model_path)
    weights = helper.load(in_model_path)
    model.set_weights(weights)

    # Train
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)

    # Metadata needed for aggregation server side
    metadata = {
        # num_examples are mandatory
        'num_examples': len(x_train),
        'batch_size': batch_size,
        'epochs': epochs,
    }

    # Save JSON metadata file (mandatory)
    save_metadata(metadata, out_model_path)

    # Save model update (mandatory)
    weights = model.get_weights()
    helper.save(weights, out_model_path)


if __name__ == "__main__":
    train(sys.argv[1], sys.argv[2])

