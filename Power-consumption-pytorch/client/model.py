import collections

import torch

from fedn.utils.helpers.helpers import get_helper

HELPER_MODULE = 'numpyhelper'
helper = get_helper(HELPER_MODULE)

from torch.nn import Linear
from torch.nn import ReLU
from torch.nn import Sigmoid
from torch.nn import Module
from torch.optim import SGD

from torch.nn.init import kaiming_uniform_
from torch.nn.init import xavier_uniform_


def compile_model():
    """ Compile the pytorch model.

    :return: The compiled model.
    :rtype: torch.nn.Module
    """
    class Net(torch.nn.Module):
        def __init__(self):
            super(Net, self).__init__()

            self.hidden1 = torch.nn.Linear(4, 64)
            kaiming_uniform_(self.hidden1.weight, nonlinearity='relu')
            self.act1 = ReLU()

            self.hidden2 = Linear(64, 32)
            kaiming_uniform_(self.hidden2.weight, nonlinearity='relu')
            self.act2 = ReLU()

            self.hidden3 = Linear(32, 1)
            xavier_uniform_(self.hidden3.weight)


        def forward(self, x):

            # input to first hidden layer
            x = self.hidden1(x)
            x = self.act1(x)

            # second hidden layer
            x = self.hidden2(x)
            x = self.act2(x)

            # third hidden layer and output
            x = self.hidden3(x)
            #x = self.act3(x) 

            return x

    # Return model
    return Net()



def save_parameters(model, out_path):
    """ Save model paramters to file.

    :param model: The model to serialize.
    :type model: torch.nn.Module
    :param out_path: The path to save to.
    :type out_path: str
    """
    parameters_np = [val.cpu().numpy() for _, val in model.state_dict().items()]
    helper.save(parameters_np, out_path)


def load_parameters(model_path):
    """ Load model parameters from file and populate model.

    param model_path: The path to load from.
    :type model_path: str
    :return: The loaded model.
    :rtype: torch.nn.Module
    """
    model = compile_model()
    parameters_np = helper.load(model_path)

    params_dict = zip(model.state_dict().keys(), parameters_np)
    state_dict = collections.OrderedDict({key: torch.tensor(x) for key, x in params_dict})
    model.load_state_dict(state_dict, strict=True)
    return model


def init_seed(out_path='seed.npz'):
    """ Initialize seed model and save it to file.

    :param out_path: The path to save the seed model to.
    :type out_path: str
    """
    # Init and save
    model = compile_model()
    save_parameters(model, out_path)


if __name__ == "__main__":
    init_seed('../seed.npz')
