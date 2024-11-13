# Python3 code to program to find occurrence
# to each character in given string

# initializing string
inp_str = "GeeksforGeeks"

# using set() + count() to get count
# of each element in string
out = {x : inp_str.count(x) for x in set(inp_str )}

# printing result
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(out))
