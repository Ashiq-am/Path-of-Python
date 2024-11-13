# importing the module
import json


# declaringa a class
class obj:

    # constructor
    def __init__(self, dict1):
        self.__dict__.update(dict1)


def dict2obj(dict1):
    # using json.loads method and passing json.dumps
    # method and custom object hook as arguments
    return json.loads(json.dumps(dict1), object_hook=obj)


# initializing the dictionary
dictionary = {'A': 1, 'B': {'C': 2},
              'D': ['E', {'F': 3}], 'G': 4}

# calling the function dict2obj and
# passing the dictionary as argument
obj1 = dict2obj(dictionary)

# accessing the dictionary as an object
print(obj1.A)
print(obj1.B.C)
print(obj1.D[0])
print(obj1.D[1].F)
print(obj1.G)
