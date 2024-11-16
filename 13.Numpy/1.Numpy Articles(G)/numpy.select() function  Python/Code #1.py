# Python program explaining
# numpy.select() function

# importing numpy as geek
import numpy as geek

arr = geek.arange(8)

condlist = [arr<3, arr>4]
choicelist = [arr, arr**3]

gfg = geek.select(condlist, choicelist)

print (gfg)
