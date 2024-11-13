try:

    # In python 2.x it is available as default
    import cPickle as pickle
except ImportError:

    # In python 3.x cPickle is not available
    import pickle

import random


# If the file is available,
# we can use import statement to import the class

# A custom class to demonstrate pickling
class ModelTrainer:
    def __init__(self) -> None:
        self.weights = [0, 0, 0]

    def train(self):
        for i in range(len(self.weights)):
            self.weights[i] = random.random()

    def get_weights(self):
        return self.weights

    # Deserialization of the file


file = open('model.pkl', 'rb')
new_model = pickle.load(file)

print('Weights of model', new_model.get_weights())
