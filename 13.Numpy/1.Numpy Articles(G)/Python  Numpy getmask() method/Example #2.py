# import numpy
import numpy.ma as ma

gfg = ma.masked_equal([11, 12, 13, 14, 15], 12)

# using numpy.getmask() method
print(ma.getmask(gfg))
