# Same list as the one used in the previous example
l = [14, 8, 0, 12, 981, 21, -99]

# The number to which all the elements of the list will be divided
divisor = 7

# This list would store the quotient of the division
# operation for corresponding elements
final = list(map(lambda x: x//divisor, l))

print(final)
