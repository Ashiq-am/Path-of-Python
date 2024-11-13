# importing library
from pgmagick.api import Image

img = Image((300, 200), 'green')
img.font("/usr/share/fonts/truetype/ttf-japanese-gothic.ttf")
img.font_pointsize(26)

# annotate function
img.annotate('GeeksforGeeks')
img.write('GeeksforGeeks.png')
