# import legendre
from numpy.polynomial import legendre

# create a complex variable
my_value = complex(4,5)

# display value
print("Complex value: ", my_value)

# generate legendary roots
print("legendary roots: ", legendre.legfromroots((-my_value, my_value)))
