

# importing image class from PIL package
import math
from PIL import ImagePath

# creating a list to getbox
getbox = list(zip(range(2, 51, 5), range(14, 25, 5)))
result = ImagePath.Path(getbox).getbbox()
print(result)
print(getbox)
