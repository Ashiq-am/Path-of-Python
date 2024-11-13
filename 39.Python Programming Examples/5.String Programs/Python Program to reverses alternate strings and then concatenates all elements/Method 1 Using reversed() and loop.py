# initializing string
test_str = 'geeksgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# spliting string
temp = test_str.split()

res = []
for idx in range(len(temp)):

    # reversing if alternate
    if idx % 2 == 0:
        res.append(''.join(list(reversed(temp[idx]))))
    else:
        res.append(temp[idx])

res = ' '.join(res)

# printing result
print("Transformed String : " + str(res))
