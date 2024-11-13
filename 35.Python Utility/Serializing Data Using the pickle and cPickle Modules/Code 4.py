try:

    # In python 2.x it is available as default
    import cPickle as pickle
except ImportError:

    # In python 3.x cPickle is not available
    import pickle

import random


# A custom class to demonstrate pickling
class ModelTrainer:
    def __init__(self) -> None:
        self.weights = [0, 0, 0]

    def train(self):
        for i in range(len(self.weights)):
            self.weights[i] = random.random()

    def get_weights(self):
        return self.weights

    # Create an object


model = ModelTrainer()

# Populate the data
model.train()

print('Weights before pickling', model.get_weights())

# Pickle the object
byte_string = pickle.dumps(model)

print("The bytes of object are:", byte_string)

# Deserialization of the object using same byte string
new_model = pickle.loads(byte_string)

print('Weights after depickling', new_model.get_weights())
