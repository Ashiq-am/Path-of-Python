# initializing List
test_list = ["geeks", "peeks", "meeks", "leeks", "mean"]

# printing original list
print("The original list is : " + str(test_list))

# initializing prefix list
pref_list = ["ge", "ne", "me", "re"]

# checking for all possible allowed prefixes using any()
# filtering using filter() and lambda
res = list(filter(lambda ele: any(ele.startswith(el)
								for el in pref_list), test_list))

# printing result
print("The extracted prefix strings list : " + str(res))
