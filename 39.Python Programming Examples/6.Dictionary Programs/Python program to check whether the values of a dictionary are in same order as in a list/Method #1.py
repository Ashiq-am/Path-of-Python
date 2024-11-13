# Python3 code to demonstrate working of
# Test for Ordered values from List
# Using loop

# initializing dictionary
test_dict = {"gfg": 4, "is": 10, "best": 11, "for": 19, "geeks": 1}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing list
sub_list = [4, 10, 11, 19, 1]

idx = 0
res = True
for key in test_dict:

    # checking for inequality in order
    if test_dict[key] != sub_list[idx]:
        res = False
        break
    idx += 1

# printing result
print("Are values in order : " + str(res))
