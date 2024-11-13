import pickle

try:
    pickle.dumps(dataset)
    pickle.dumps(model)
except pickle.PicklingError:
    print("Error: The dataset or model is not compatible with multiprocessing.")
