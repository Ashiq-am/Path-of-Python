# import legendre
from numpy.polynomial import legendre

# create a complex variable
my_value = complex(45,4)

# display value
print("Complex value: ", my_value)

# generate legendary roots
print("legendary roots: ", legendre.legfromroots(
(-my_value, my_value)))

# get the dimensions
print("Dimensions: ", legendre.legfromroots(
(-my_value, my_value)).ndim)

# get the shape
print("shape: ",legendre.legfromroots(
(-my_value, my_value)).shape)
