# Python program to copy a nested list

# List initialization
Input_list = [[0,1,2], [3,4,5], [0, 1, 8]]

# comprehensive method
out_list = [ele[:] for ele in Input_list]

# Printing Output
print("Initial list is:")
print(Input_list)
print("New assigned list is")
print(out_list)
