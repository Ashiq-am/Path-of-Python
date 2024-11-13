# importing the required module
import random

# converting the list into a set
Set = set([10, 20, 30, 40, 50, 40, 30, 20, 10])

# using the choices() method on the
# given dataset
UpdatedList = random.choices(list(Set), k = 3)

# displaying random selections without
# repetition
print(UpdatedList)
