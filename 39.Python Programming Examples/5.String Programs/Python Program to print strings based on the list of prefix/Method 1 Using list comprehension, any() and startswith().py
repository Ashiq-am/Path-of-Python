# initializing List
test_list = ["geeks", "peeks", "meeks", "leeks", "mean"]

# printing original list
print("The original list is : " + str(test_list))

# initializing prefix list
pref_list = ["ge", "ne", "me", "re"]

# checking for all possible allowed prefixes using any()
res = [ele for ele in test_list if any(ele.startswith(el) for el in pref_list)]

# printing result
print("The extracted prefix strings list : " + str(res))
