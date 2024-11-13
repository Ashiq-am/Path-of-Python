# Python code to convert list of tuples into list

# List of tuple initialization
lt = [('Geeks', 2), ('For', 4), ('geek', '6')]

# using list comprehension
out = [item for t in lt for item in t]

# printing output
print(out)
