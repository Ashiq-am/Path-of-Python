

# from PIL importing ImagePath
from PIL import ImagePath

# creating a list to map
getbox = list(zip(range(5, 51, 16), range(15, 22, 4)))
result = ImagePath.Path(getbox)

# using tolist function
a = result.tolist()
print(getbox)
print(a)
