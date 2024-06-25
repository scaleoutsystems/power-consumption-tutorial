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

dir_path = os.path.dirname(os.path.realpath(__file__))
abs_path = os.path.abspath(dir_path)


def validate(in_model_path, out_json_path, data_path=None):
    """ Validate model.

    :param in_model_path: The path to the input model.
    :type in_model_path: str
    :param out_json_path: The path to save the output JSON to.
    :type out_json_path: str
    :param data_path: The path to the data file.
    :type data_path: str
    """

    # Load data
    x_train, y_train = load_data(data_path)
    x_test, y_test = load_data(data_path, is_train=False)

    # Load model
    model = compile_model()
    helper = get_helper(HELPER_MODULE)
    weights = helper.load(in_model_path)
    model.set_weights(weights)

    # Evaluate
    model_score_train = model.evaluate(x_train, y_train)
    model_score_test = model.evaluate(x_test, y_test)

    # JSON schema
    report = {
        "training_mse": model_score_train[0],
        "test_mse": model_score_test[0]
    }

    # Save JSON
    save_metrics(report, out_json_path)

if __name__ == "__main__":
    validate(sys.argv[1], sys.argv[2])
