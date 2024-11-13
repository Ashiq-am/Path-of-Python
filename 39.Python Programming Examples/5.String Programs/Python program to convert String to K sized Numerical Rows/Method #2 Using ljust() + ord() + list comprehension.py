from math import ceil

# initializing string
test_str = 'geeksforgeekscse'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

# filling the rear to K size rows
temp = test_str.ljust(ceil(len(test_str) / K) * K)

# convert to numerical characters
temp = [0 if char == ' ' else (ord(char) - 97) for char in temp]

# slice and render to matrix
res = [temp[idx: idx + K] for idx in range(0, len(temp), K)]

# printing result
print("Grouped and Converted String : " + str(res))
