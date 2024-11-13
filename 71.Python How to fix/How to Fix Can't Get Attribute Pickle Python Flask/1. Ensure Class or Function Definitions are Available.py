# mymodule.py
class MyClass:
    def __init__(self, data):
        self.data = data

# app.py
import pickle
from mymodule import MyClass

with open('mydata.pkl', 'rb') as f:
    obj = pickle.load(f)
