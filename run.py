import os
import multiprocessing

import numpy as np
import pandas as pd

import input
import model
import training
import output
import utils


def run(config):
    print(config)


def main():
    file, parallel = utils.run.parse_args()
    file_extension = os.path.splitext(file)[1]

    if parallel:
        print("Running in parallel")
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            run_configs = [config for config in utils.run.load_run_config_files(file)]
            pool.map(run, run_configs)

    elif file_extension == ".txt":
        print("Running in sequential")
        run_configs = [config for config in utils.run.load_run_config_files(file)]
        for run_config in run_configs:
            run(run_config)

    else:
        print("Running")
        run(file)


if __name__ == "__main__":
    main()
