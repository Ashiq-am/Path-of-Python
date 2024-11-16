# Python program explaining
# numpy.select() function

# importing numpy as geek
import numpy as geek

arr = geek.arange(8)

condlist = [arr<4, arr>6]
choicelist = [arr, arr**2]

gfg = geek.select(condlist, choicelist)

print (gfg)
