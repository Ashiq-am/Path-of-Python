# importing library
from pgmagick.api import Image

# using image function
img = Image((300, 300), 'green')
img.annotate('GeeksforGeeks')
img.write('GeeksforGeeks.jpg')
