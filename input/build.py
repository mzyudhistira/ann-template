import importlib


class Input:
    def __init__(self, input_param) -> None:
        self.module = input_param["module"]
        self.generator = input_param["generator"]
        self.param = input_param["param"]
        self.tensor = None
        print(self.module, self.generator, self.param)

    def generate_input_data(self):
        module = importlib.import_module(self.module)
        generator = getattr(module, self.generator)

        input_data = generator(self.param)

        return input_data
