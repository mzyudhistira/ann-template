import numpy as np
from tensorflow.keras.datasets import boston_housing

from . import preprocess


def boston_housing_case(input_param):
    """
    Generate boston housing data

    Args:
        input_param (dict): Parameters of the generator

    Returns:
        data_train, data_val, data_test (tuple of np arr):
        Train, validation and test data. The tuple consists of
        feature and target data.
    """
    percent_train, percent_val, percent_test = input_param["percentage"]
    (X_train, y_train), (X_test, y_test) = boston_housing.load_data()

    # Combine all the data, then split using the prepared method
    xy_train = np.concatenate((X_train, y_train.reshape(-1, 1)), axis=1)
    xy_test = np.concatenate((X_test, y_test.reshape(-1, 1)), axis=1)
    input_data = np.concatenate((xy_train, xy_test), axis=0)

    # Preprocessing
    input_data = preprocess.normalise(input_data)
    data_train, data_val, data_test = preprocess.split(
        input_data, percent_train, percent_val, percent_test
    )

    return (
        extract_feature(data_train),
        extract_feature(data_val),
        extract_feature(data_test),
    )


def extract_feature(data):
    return data[:, :-1], data[:, -1]
