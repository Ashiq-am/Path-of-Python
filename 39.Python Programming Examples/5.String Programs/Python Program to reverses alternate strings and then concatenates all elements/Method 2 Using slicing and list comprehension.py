# initializing string
test_str = 'geeksgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# spliting string
temp = test_str.split()

# list comprehension to solve problem in 1 liner
res = ' '.join([''.join(list(reversed(temp[idx]))) if idx % 2 == 0 else temp[idx] for idx in range(len(temp))])

# printing result
print("Transformed String : " + str(res))
