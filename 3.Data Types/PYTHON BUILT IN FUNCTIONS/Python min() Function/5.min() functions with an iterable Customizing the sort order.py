# Python code to demonstrate the
# working of min()


d = {1: "c", 2: "b", 3: "a"}

# printing the minimum key of
# dictionary
print(min(d))

# printing the key with minimum
# value in dictionary
print(min(d, key=lambda k: d[k]))
