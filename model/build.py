import importlib


class Model:
    def __init__(self, input_object, model_param) -> None:
        self.module = model_param["module"]
        self.generator = model_param["generator"]
        self.param = model_param["param"]
        self.model = None
        print(self.module, self.generator, self.param)

    def generate_model(self):
        pass
