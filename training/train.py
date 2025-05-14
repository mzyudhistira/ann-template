import importlib


class TrainModel:
    def __init__(self, input_object, model_object, training_param) -> None:
        self.module = training_param["module"]
        self.method = training_param["method"]
        self.param = training_param["param"]
        self.best_weight = None
        self.last_weight = None
        self.loss = None
        self.val_loss = None
        print(self.module, self.method, self.param)

    def run_training(self):
        pass
