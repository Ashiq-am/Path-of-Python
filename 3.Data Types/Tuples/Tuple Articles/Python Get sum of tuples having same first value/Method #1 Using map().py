# Python code to get sum of tuples having same first value

# Initialisation of list of tuple
Input = [(1, 13), (1, 190), (3, 25), (1, 12)]

d = {x:0 for x, _ in Input}

for name, num in Input: d[name] += num

# using map
Output = list(map(tuple, d.items()))

# printing output
print(Output)
