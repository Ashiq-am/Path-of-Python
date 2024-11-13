import cloudpickle as pickle

# Saving an object
with open('mydata.pkl', 'wb') as f:
    pickle.dump(my_object, f)

# Loading an object
with open('mydata.pkl', 'rb') as f:
    obj = pickle.load(f)
