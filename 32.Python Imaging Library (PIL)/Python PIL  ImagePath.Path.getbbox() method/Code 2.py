

# importing image class from PIL package
import math
from PIL import ImagePath

# creating a list to getbox
getbox = list(zip(range(3, 41, 1), range(11, 22, 2)))
result = ImagePath.Path(getbox).getbbox()
print(result)
print(getbox)
