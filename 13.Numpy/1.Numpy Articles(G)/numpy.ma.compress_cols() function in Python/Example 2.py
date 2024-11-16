# importing numpy as geek
import numpy as geek

# defining array
arr = geek.ma.array(geek.arange(9).reshape(3, 3), mask=[
					[1, 0, 0], [1, 0, 0], [0, 0, 0]])

# applying mask to array elements
gfg = geek.ma.compress_cols(arr)

print(gfg)
