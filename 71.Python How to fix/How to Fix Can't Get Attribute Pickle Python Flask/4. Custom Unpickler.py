import pickle

class MyCustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__":
            module = "mymodule"
        return super().find_class(module, name)

with open('mydata.pkl', 'rb') as f:
    unpickler = MyCustomUnpickler(f)
    obj = unpickler.load()
