

# from PIL importing ImagePath
from PIL import ImagePath

# creating a list to map
getbox = list(zip(range(3, 41, 1), range(11, 22, 2)))
result = ImagePath.Path(getbox)

# using map function
b = result.map(lambda x, y: (x + 2, y + 2))
a = result.tolist()
print(a)
