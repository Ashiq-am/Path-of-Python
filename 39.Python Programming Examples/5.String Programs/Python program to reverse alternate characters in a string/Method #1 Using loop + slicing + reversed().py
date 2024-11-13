# Python3 code to demonstrate working of
# Alternate characters reverse in String
# Using loop + slicing + reversed()

# initializing string
test_str = 'geeks4rgeeks'

# printing original string
print("The original string is : " + str(test_str))

# extracting alternate string
alt = test_str[::2]
not_alt = test_str[1::2]

# performing reverse
alt = "".join(reversed(alt))

res = ''
# remaking string
for idx in range(len(alt)):
    res += alt[idx]
    res += not_alt[idx]

# printing result
print("Is alternate reversed string : " + str(res))
