# Python3 code to demonstrate working of
# Sort Matrix by total characters
# Using sorted() + lambda

# initializing list
test_list = [["Gfg", "is", "Best"], ["Geeksforgeeks", "Best"],
			["GFg", "4", "good"], ["ILvGFG"]]

# printing original list
print("The original list is : " + str(test_list))

# sorted() gives sorted result
# lambda function providing logic
res = sorted(test_list, key = lambda row : sum([len(sub) for sub in row]))

# printing result
print("Sorted results : " + str(res))
