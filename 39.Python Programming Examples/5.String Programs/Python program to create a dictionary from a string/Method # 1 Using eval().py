# Python3 code to convert
# a string to a dictionary

# Initializing String
string = "{'A':13, 'B':14, 'C':15}"

# eval() convert string to dictionary
Dict = eval(string)
print(Dict)
print(Dict['A'])
print(Dict['C'])
