# app.py
import pickle

class MyClass:
    def __init__(self, data):
        self.data = data

if __name__ == "__main__":
    with open('mydata.pkl', 'rb') as f:
        obj = pickle.load(f)
