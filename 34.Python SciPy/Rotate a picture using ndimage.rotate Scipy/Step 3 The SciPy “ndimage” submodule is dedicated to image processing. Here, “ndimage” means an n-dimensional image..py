from scipy import ndimage, misc
from matplotlib import pyplot as plt
panda = misc.face()

#image rotated 135 degree
panda_rotate = ndimage.rotate(panda, 135, mode = 'constant')
