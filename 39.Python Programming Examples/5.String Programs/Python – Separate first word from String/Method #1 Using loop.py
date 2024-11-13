# Python3 code to demonstrate working of
# Separate first word from String
# Using loop

# initializing string
test_str = "gfg is best"

# printing original string
print("The original string is : " + test_str)

# Separate first word from String
# Using loop
res = []
temp = ''
flag = 1
for ele in test_str:
    if ele == ' ' and flag:
        res.append(temp)
        temp = ''
        flag = 0
    else:
        temp += ele
res.append(temp)

# printing result
print("Initial word separated list : " + str(res))
