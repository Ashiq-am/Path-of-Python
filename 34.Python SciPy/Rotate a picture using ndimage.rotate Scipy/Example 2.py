from scipy import ndimage, misc
from matplotlib import pyplot as plt

panda = misc.ascent()

#image rotated 360 degree
panda_rotate = ndimage.rotate(panda, 45,
							mode = 'constant')
plt.imshow(panda_rotate)
plt.show()
