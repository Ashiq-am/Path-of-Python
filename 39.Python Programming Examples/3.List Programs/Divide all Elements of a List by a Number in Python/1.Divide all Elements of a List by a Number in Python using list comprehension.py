# Same list as the one used in the previous example
l = [14, 8, 0, 12, 981, 21, -99]

# The number to which all the elements of the list will be divided
divisor = 7

# Performing list comprehension and saving the
# result in a separate variable
result = [x//divisor for x in l]

print(result)
