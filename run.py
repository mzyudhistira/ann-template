import os
import multiprocessing
from datetime import datetime
import csv

import numpy as np
import pandas as pd

import input
import model
import training
import output
import utils


def run(config):
    """

    Args:
        config (str): Location of the TOML run configuration file

    Returns:
        run_summary (list): List of strings summarizing the run:
                            datetime, run name, run config file, loss, validation loss,
                            rms deviation, std difference, output file, and note

    """

    # Load run config
    run_param = utils.run.load_param(config)
    run_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Initialize the directories
    utils.file.initialize_directory()
    utils.file.initialize_run_result_dir(run_param, run_datetime)

    # Running the pipeline
    input_obj = input.build.Input(run_param["input"])
    model_obj = model.build.Model(input_obj, run_param["model"])
    model_obj.model.summary()
    # train_obj = training.train.TrainModel(input_obj, model_obj, run_param["training"])
    # test_result = output.test.Test(input_obj, model_obj, train_obj)

    # Writing run summary
    # run_summary = [
    #     run_datetime,
    #     run_param["run"]["name"],
    #     config,
    #     train_obj.loss,
    #     train_obj.val_loss,
    #     test_result.rms_dev,
    #     test_result.std_diff,
    #     test_result.output,
    #     run_param["run"]["note"],
    # ]
    #
    # with open("summary.csv", "a", newline="") as summary_file:
    #     writer = csv.writer(summary_file)
    #
    #     run_summary = [
    #         [x if x is not None else "" for x in run_summary]
    #     ]  # Replace None with empty string
    #     writer.writerows(run_summary)
    #
    # return run_summary
    #


def main():
    file, parallel = utils.run.parse_args()
    file_extension = os.path.splitext(file)[1]
    multiple_run_configs = file_extension == ".txt"

    if multiple_run_configs and parallel:
        print("Running in parallel")
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            run_configs = [config for config in utils.run.load_run_config_files(file)]
            pool.map(run, run_configs)

    elif multiple_run_configs:
        print("Running in sequential")
        run_configs = [config for config in utils.run.load_run_config_files(file)]
        for run_config in run_configs:
            run(run_config)

    else:
        print("Running")
        run(file)


if __name__ == "__main__":
    main()
