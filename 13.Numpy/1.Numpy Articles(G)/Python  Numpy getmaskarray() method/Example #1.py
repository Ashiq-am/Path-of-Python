# import numpy
import numpy.ma as ma

gfg = ma.masked_equal([[1, 2], [5, 6]], 5)

# using numpy.getmaskarray() method
print(ma.getmaskarray(gfg))
