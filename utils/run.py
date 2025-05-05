import os
import argparse
import multiprocessing

import toml


def load_param(run_param_file):
    with open(run_param_file, "r") as f:
        config = toml.load(f)

    return config


def load_run_config_files(params_list_file):
    with open(params_list_file, "r") as f:
        config_files = [line.strip() for line in f if line.strip()]

    return config_files


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file", help="Run configuration file in TOML or TXT (see documentation)"
    )
    parser.add_argument(
        "-pl",
        "--parallel",
        help="Run the program in parallel, only accept TXT",
        action="store_true",
    )

    args = parser.parse_args()

    if args.parallel and not args.file.lower().endswith(".txt"):
        parser.error("Parallel mode only supports TXT files.")

    return args.file, args.parallel
