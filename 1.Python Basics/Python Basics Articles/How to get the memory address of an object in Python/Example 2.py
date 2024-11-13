# import addressof and c_int modules
# from ctypes module
from ctypes import c_int, addressof

# get memory address of variable
a = 44
print(addressof(c_int(a)))
