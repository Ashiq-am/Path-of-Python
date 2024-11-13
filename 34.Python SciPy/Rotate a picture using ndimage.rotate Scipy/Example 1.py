from scipy import ndimage, misc
from matplotlib import pyplot as plt

panda = misc.face()
#image rotated 35 degree
panda_rotate = ndimage.rotate(panda, 35,
							mode = 'mirror')
plt.imshow(panda_rotate)
plt.show()
