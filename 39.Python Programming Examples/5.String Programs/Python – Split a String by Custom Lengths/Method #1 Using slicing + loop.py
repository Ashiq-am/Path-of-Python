# Python3 code to demonstrate working of
# Multilength String Split
# Using loop + slicing

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing length list
cus_lens = [5, 3, 2, 3]

res = []
strt = 0
for size in cus_lens:
    # slicing for particular length
    res.append(test_str[strt: strt + size])
    strt += size

# printing result
print("Strings after splitting : " + str(res))
