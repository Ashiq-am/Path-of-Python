# importing module
from pgmagick.api import Image

img = Image('koala.jpeg')
img.edge(1)
img.write('edge_koala.jpeg')
