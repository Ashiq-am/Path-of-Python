# initializing dictionary
test_dict = {"Gfg" : [6, 2, 4, 1], "is" : [4, 7, 3, 3, 8], "Best" : [1, 0, 9, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# getting max value
max_res = max([max(vals) - min(vals) for sub, vals in test_dict.items()])

# getting key matching with maximum value
res = [sub for sub in test_dict if max(test_dict[sub]) - min(test_dict[sub]) == max_res][0]

# printing result
print("The maximum element key : " + str(res))
