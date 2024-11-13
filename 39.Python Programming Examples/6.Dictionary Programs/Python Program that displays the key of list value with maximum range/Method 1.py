# initializing dictionary
test_dict = {"Gfg": [6, 2, 4, 1], "is": [4, 7, 3, 3, 8], "Best": [1, 0, 9, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

max_res = 0
for sub, vals in test_dict.items():

    # storing maximum of difference
    max_res = max(max_res, max(vals) - min(vals))
    if max_res == max(vals) - min(vals):
        res = sub

# printing result
print("The maximum element key : " + str(res))
