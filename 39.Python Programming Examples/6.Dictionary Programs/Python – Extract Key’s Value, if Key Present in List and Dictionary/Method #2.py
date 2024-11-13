# Python3 code to demonstrate working of
# Extract Key's Value, if Key Present in List and Dictionary
# Using set() + intersection()

# initializing list
test_list = ["Gfg", "is", "Good", "for", "Geeks"]

# initializing Dictionary
test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

# initializing K
K = "Gfg"

# printing original list and Dictionary
print("The original list : " + str(test_list))
print("The original Dictionary : " + str(test_dict))

# conversion of lists to set and intersection with keys
# using intersection
res = None
if K in set(test_list).intersection(test_dict):
	res = test_dict[K]

# printing result
print("Extracted Value : " + str(res))
