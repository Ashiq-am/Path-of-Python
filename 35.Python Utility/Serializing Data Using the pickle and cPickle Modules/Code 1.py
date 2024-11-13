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

# Open a file to write bytes
p_file = open('model.pkl', 'wb')

# Pickle the object
pickle.dump(model, p_file)
p_file.close()

# Deserialization of the file
file = open('model.pkl', 'rb')
new_model = pickle.load(file)

print('Weights after pickling', new_model.get_weights())
