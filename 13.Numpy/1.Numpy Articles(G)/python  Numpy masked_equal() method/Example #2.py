# import numpy
import numpy.ma as ma

# using numpy.ma.masked_equal() method
gfg = ma.masked_equal([[1, 2, 3, 4],
					[6, 7, 8, 9]], 6)

print(gfg)
