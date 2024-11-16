# Python program explaining
# numpy.core.defchararray.translate() method

# importing numpy
import numpy as geek

# input array
in_arr = geek.array(['Weeks', 'our', 'Weeks'])
print("Input original array : ", in_arr)

# creating dictionary for translation table
trans_dict = {"W": "G", "o": "f", "u": "o"}

# creating translation table from dictionary
trans_table = "Wou".maketrans(trans_dict)

out_arr = geek.core.defchararray.translate(in_arr, trans_table, deletechars="None")
print("Output translated array: ", out_arr)
