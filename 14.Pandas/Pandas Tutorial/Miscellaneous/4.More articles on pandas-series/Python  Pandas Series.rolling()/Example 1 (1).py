# Find sum over a window size of 2
result = sr.rolling(2).sum()

# Print the returned Series object
print(result)
