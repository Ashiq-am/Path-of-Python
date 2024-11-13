# Python3 code to demonstrate working of
# Concatenate Strings on K String
# Using loop

# initializing list
test_list = ["Gfg", "+", "is", "best", "+", "love", "gfg"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K for Concatenate
K = "+"

res = []
idx = 0

while idx < len(test_list):

    ele = test_list[idx]

    # concatenation if next symbol is K
    if (idx < len(test_list) - 1) and test_list[idx + 1] == K:
        ele = ele + K + test_list[idx + 2]

        # increasing counter by 2
        idx += 2
    res.append(ele)
    idx += 1

# printing result
print("Strings after required concatenation : " + str(res))
