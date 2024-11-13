# initializing string
test_str = 'geeksforgeeks best for geeks'

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 2

# getting Kth element of each word
temp = []
for sub in test_str.split():
    temp.append(sub[K])

# joining together
res = ''.join(temp)

# printing result
print("The K joined String is : " + str(res))
