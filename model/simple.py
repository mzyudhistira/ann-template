import tensorflow as tf
from keras import models, layers, Input


def sequential(
    N_input,
    neurons,
    activation_function="relu",
    optimizer="rmsprop",
    loss="mse",
    metrics=["mae"],
):
    """

    Args:
        N_input (int): The number of input data
        neurons (list): A list of neurons for every hidden layers
        activation_function (keras activation function): Activation function for hidden layers, default to 'relu'
        optimizer (keras optimizer): Optimzier for the training, defaults to 'rmsprop'
        loss (keras loss): Loss function, defaults to 'mse'
        metrics (keras metrics): Metrics to be shown during training, defaults to ['mae']

    Returns:
        model (keras model)
    """
    model = models.Sequential()
    model.add(Input(shape=(N_input,)))

    for neuron in neurons:
        model.add(layers.Dense(neuron, activation=activation_function))

    model.add(layers.Dense(1))
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    return model
