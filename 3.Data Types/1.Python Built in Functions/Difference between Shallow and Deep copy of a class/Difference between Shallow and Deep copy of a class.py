# Python3 implementation of the Deep
# copy and Shallow Copy
from copy import copy, deepcopy


# Class of Car
class Car:
    def __init__(self, name, colors):
        self.name = name
        self.colors = colors


honda = Car("Honda", ["Red", "Blue"])

# Deepcopy of Honda
deepcopy_honda = deepcopy(honda)
deepcopy_honda.colors.append("Green")
print(deepcopy_honda.colors, honda.colors)

# Shallow Copy of Honda
copy_honda = copy(honda)

copy_honda.colors.append("Green")
print(copy_honda.colors, honda.colors)
