# import numpy.ma
import numpy.ma as ma

# using numpy.ma.ids() method
gfg = ma.array([1, 2, 4, 8], mask =[1, 0, 0, 1])

print(gfg.ids())
