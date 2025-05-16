import time

import numpy as np
from keras.callbacks import ModelCheckpoint, Callback


def simple(training_data, training_param, model, validation_data, file):
    """
    Simple training method

    Args:
        training_data (tuple): Feature and target of the training data
        training_param (dict): Parameter of the training
        model (model object): Model object from the pipeline
        validation_data (tuple): Feature and target of the validation data
        file (list): Filepath of the results
    """
    best_weights, last_weights, loss_path, val_loss_path = file

    features, target = training_data
    val_features, val_target = validation_data

    epoch = training_param["epoch"]
    batch = training_param["batch"]

    model_checkpoint_callback = ModelCheckpoint(
        save_weights_only=True,
        save_best_only=True,
        monitor="val_mae",
        mode="min",
        filepath=best_weights,
    )

    history = model.fit(
        features,
        target,
        validation_data=(val_features, val_target),
        batch_size=batch,
        epochs=epoch,
        verbose=2,
        callbacks=[model_checkpoint_callback],
    )

    model.save_weights(last_weights)
    np.savetxt(loss_path, history.history["loss"])
    np.savetxt(val_loss_path, history.history["val_loss"])


def multi_stage():

    return
