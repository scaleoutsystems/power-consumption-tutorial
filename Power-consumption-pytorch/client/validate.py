import os
import sys

import torch
from data import load_data
from model import load_parameters

import numpy as np

from fedn.utils.helpers.helpers import save_metrics

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(dir_path))


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
    model = load_parameters(in_model_path)
    model.eval()

    # Evaluate
    criterion_mae = torch.nn.L1Loss()
    criterion_mse = torch.nn.MSELoss()
    with torch.no_grad():
        x_train_t = torch.tensor(x_train, dtype=torch.float32)
        train_out = model(x_train_t)

        y_train = torch.from_numpy(np.expand_dims(y_train,-1))
        y_train_t = torch.tensor(y_train, dtype=torch.float32)

        training_loss_mae = criterion_mae(train_out, y_train_t)
        training_loss_mse = criterion_mse(train_out, y_train_t)

        x_test_t = torch.tensor(x_test, dtype=torch.float32)
        test_out = model(x_test_t)

        y_test = torch.from_numpy(np.expand_dims(y_test,-1))
        y_test_t = torch.tensor(y_test, dtype=torch.float32)

        test_loss_mae = criterion_mae(test_out, y_test_t)
        test_loss_mse = criterion_mse(test_out, y_test_t)  

    # JSON schema
    report = {
        "test_mae": str(test_loss_mae.item()),
        "test_mse": str(test_loss_mse.item()),
        "training_mae": str(training_loss_mae.item()),
        "training_mse": str(training_loss_mse.item()),

    }

    # Save JSON
    save_metrics(report, out_json_path) 

if __name__ == "__main__":
    validate(sys.argv[1], sys.argv[2])
