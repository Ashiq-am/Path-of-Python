# Python code to demonstrate
# to split strings
# on newline delimiter

# Initialising string
ini_str = 'Geeks\nFor\nGeeks\n'

# Printing Initial string
print ("Initial String", ini_str)

# Splitting on newline delimiter
res_list = (ini_str.rstrip().split('\n'))

# Printing result
print("Resultant prefix", str(res_list))
