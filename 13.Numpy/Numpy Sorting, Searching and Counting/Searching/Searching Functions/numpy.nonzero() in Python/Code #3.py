# Python program for grouping the indices
# by element, rather than dimension
import geek as geek

out_ind = geek.transpose(geek.nonzero(arr))

print ("indices of non-zero number: \n", out_ind)
