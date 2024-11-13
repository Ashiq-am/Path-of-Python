# Python3 code to demonstrate working of
# Equal character frequencies
# Using max() + count() + loop

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# getting maximum frequency character
max_freq = max([test_str.count(ele) for ele in test_str])

# equating frequencies
res = test_str
for chr in test_str:

    # if frequencies don't match max_freq
    if res.count(chr) != max_freq:
        res += chr * (max_freq - test_str.count(chr))

    # printing result
print("Equal character frequency String : " + str(res))
