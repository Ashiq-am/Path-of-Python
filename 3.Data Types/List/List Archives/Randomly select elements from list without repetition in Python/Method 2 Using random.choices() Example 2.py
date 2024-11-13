# importing the required module
import random

# converting the list into set
List = [i for i in range(1, 100)]

# using the choices() method on a
# sequence of numbers
UpdatedList = random.choices(List, k = 5)

# displaying random selections without
# repetition
print(UpdatedList)
