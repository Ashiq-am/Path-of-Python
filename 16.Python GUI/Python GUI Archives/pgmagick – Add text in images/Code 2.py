# importing library
from pgmagick.api import Image

img = Image((300, 300), 'green')

# annotate function
img.annotate('GeeksforGeeks', angle = 45)
img.write('geeksforgeeks.png')
