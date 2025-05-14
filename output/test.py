import importlib


class Test:
    def __init__(self, input_obj, model_obj, train_obj) -> None:
        self.rms_dev = None
        self.std_diff = None
        self.output = None
