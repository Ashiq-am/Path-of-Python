# Python code to truncate float
# values to 2 decimal digits.

# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]

# Using map
Output = map(lambda n: "%.2f" % n, Input)

# Converting to list
Output = list(Output)

# Print output
print(Output)
