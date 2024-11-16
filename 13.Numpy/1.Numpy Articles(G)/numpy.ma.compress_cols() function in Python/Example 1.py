# importing numpy as geek
import numpy as geek

# defining an array with mask
arr = geek.ma.array(geek.arange(6).reshape(2, 3),
					mask=[[1, 0, 0], [0, 0, 0]])

# applying mask to array elements
gfg = geek.ma.compress_cols(arr)

print(gfg)
