try:
    # In python 2.x it is available as default
    import cPickle as pickle
except ImportError:

    # In python 3.x cPickle is not available
    import pickle

# Deserialization of the file
file = open('model.pkl', 'rb')
new_model = pickle.load(file)

print('Weights of model', new_model.get_weights())
