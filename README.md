# Power consumption prediction for data centers (TensorFlow/Keras)

This is an example of a neural network regression model in a federated setting. Time series data from two data centers in Sweden and Finland are used to predict the relationship between CPU and Network usage and power consumption. The tutorial is based on the following article that has more backgroud information on the use-case: 

- Towards Smart e-Infrastructures, A Community Driven Approach Based on Real Datasets
https://ieeexplore.ieee.org/document/9289758

The model in this example is a simplified version of the model used in the article, to reduce the compute requirements client side. A normal laptop or a workstation should be able to sustain a few clients. The dataset required for this example is not available on a public server. However, Scaleout support staff can provide you with the data. Feel free to contact us. 

## Prerequisites

- [Python 3.8, 3.9 or 3.10](https://www.python.org/downloads)
- [Docker](https://docs.docker.com/get-docker)

The example assumes working experience with Docker. 

## Clone the repository

```
git clone https://github.com/scaleoutsystems/Power-consumption-tutorial.git
```

## Attach clients to an existing FEDn Network (for workshop)

### Using Docker (not for M1, M2 macosx and Windows)

Here we assume that the FEDn network is up and running and you have obtained the connection file (client.yaml). In case you are participating in a Scaleout workshop, you will obtain the file from the workshop organizer. If you are working on the tutorial on your own, complete the instructions below before connecting the client.

The following command will connect your client to the FEDn network specified in client.yaml. Please fix the path of the power.npz and client.yaml files according to your local setup.

```sh
 docker run -v $PWD/client.yaml:/app/client.yaml -v $PWD/data:/var/data -e ENTRYPOINT_OPTS=--data_path=/var/data/power.npz ghcr.io/scaleoutsystems/power-consumption:main fedn run client --secure=True --force-ssl -in client.yaml 
```

### Using Docker on Windows

Here we assume that the FEDn network is up and running and you have obtained the connection file (client.yaml). In case you are participating in a Scaleout workshop, you will obtain the file from the workshop organizer. If you are working on the tutorial on your own, complete the instructions below in the section (Setting up the federation (model initiator)) before connecting the client.

Start `PowerShell` and install `virtualenv` if needed, then create a `virtualenv` named `scaleout_test` and activate it (just type deactivate to deactivate the virtualenv))

```sh
pip install virtualenv
python -m venv scaleout_test
scaleout_test/Scripts/activate
cd scaleout_test
```

Clone this repository

```sh
git clone https://github.com/scaleoutsystems/Power-consumption-tutorial.git
```

Download the dataset and client.yaml file and move them to the 'Power-consumption-tutorial' directory. The directory structure will look as follows:

```
 Dockerfile
 README.md
 bin
 client
 client.yaml
 data
 requirements.txt
 requirements-osx-m1.txt
```

where the 'data' directory contains the 'power.npz' file.

The following command will connect your client to the FEDn network specified in client.yaml. Please fix the path of the power.npz and client.yaml files according to your local setup.

```sh
docker run -v $PWD/client.yaml:/app/client.yaml -v $PWD/data:/var/data -e ENTRYPOINT_OPTS=--data_path=/var/data/power.npz --network=fedn_default ghcr.io/scaleoutsystems/power-consumption:main fedn run client --secure=True --force-ssl -in client.yaml -in client.yaml --name client1
```

### Nativly on your host (without docker)

Clone this repository
```
git clone https://github.com/scaleoutsystems/Power-consumption-tutorial.git
```

Create virtual env (from root folder in the repository)

On *Linux*:
```
bin/init_venv.sh
```

On *MacOS* (tested on M1 macs): 
```
bin/init_venv_macos.sh
```

Install FEDn into the virtual env
```
.power-consumption-keras/bin/pip install git+https://github.com/scaleoutsystems/fedn.git@master#egg=fedn\&subdirectory=fedn
```

Activate the virtual env
```
source .power-consumption-keras/bin/activate
```

Specify absolute path to your local data is located (replace /path/to/)
```
export ENTRYPOINT_OPTS=--data_path=/path/to/power.npz
```

Start the client (assumes you have the client config file client.yaml)
```
fedn run client --secure=True --force-ssl -in client.yaml
```

## Extra (not for workshop): Setting up the federation (model initiator) 

These instructions are for users that want to learn to deploy and intiatialize the federated network (model initiator). 

### Creating the federated learning network
There are two main options to deploy a FEDn network: 

1. Obtain an account in Scaleout Studio. Apply here: [https://studio.scaleoutsystems.com/signup/](https://studio.scaleoutsystems.com/signup/) and contact Scaleout staff in the [Discord server](https://discord.gg/KMg4VwszAd) for this option. 
2. [Deploy a FEDn network from scratch](https://github.com/scaleoutsystems/fedn) on your own machine(s). 

### Preparing the environment, the compute package and the seed model.

Clone above-mentioned FEDn repository in step-2. Locate into the directory, pick one of the available examples, then:

Initialize a virtual enviroment with all of the required dependencies.
```sh
bin/init_venv.sh
```

Build the compute package and seed model. 
```sh
bin/build.sh
```
You should now have two files, 'package.tar.gz' and 'seed.npz'. Initialize the FEDn network using these, and then follow instructions above to connect clients. 

Build the environment (Docker image) 
```sh
docker build -t scaleoutsystems/power-consumption:main
```

(If you have not made local changes to the package and/or requirements.txt, you can also use the pre-build package available in this repository, ghcr.io/scaleoutsystems/power-consumption:main)

You can now connect the client following the instructions above. Note that depending on how you deployed the network, you might need to modify some of the command line options to fedn. Refer to the [FEDn documentation](https://github.com/scaleoutsystems/fedn). 

