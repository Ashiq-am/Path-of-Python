import re
newData = "GeeksforGeeks, is_an-awesome ! app + too"

# To split "+" use backslash
print(re.split(', |_|-|!|\+', newData))
