# using numpy
import numpy as np

# creating own function
def fxn(val):
    return (val % 2)

# adding into numpy
mod_2 = np.frompyfunc(fxn, 1, 1)

# creating nummpy array
arr = np.arange(1, 11)
print("arr	 :", *arr)

# using function over nummpy array
mod_arr = mod_2(arr)
print("mod_arr :", *mod_arr)
