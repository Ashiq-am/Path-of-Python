# Find sum over a window size of 2
# We have also provided the window type
result = sr.rolling(2, win_type ='triang').sum()

# Print the returned Series object
print(result)
