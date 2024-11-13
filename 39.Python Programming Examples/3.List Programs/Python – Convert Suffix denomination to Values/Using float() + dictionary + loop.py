# Python3 code to demonstrate working of
# Convert Suffix denomination to Values
# Using float() + dictionary + loop

# initializing list
test_list = ["25Cr", "7M", "24B", "9L", "2Tr", "17K"]

# printing original list
print("The original list is : " + str(test_list))

# initializing values dictionary
val_dict = {"M": 1000000, "B": 1000000000, "Cr": 10000000,
			"L": 100000, "K": 1000, "Tr": 1000000000000}

res = []
for ele in test_list:
	for key in val_dict:
		if key in ele:

			# conversion of dictionary keys to values
			val = float(ele.replace(key, "")) * val_dict[key]
			res.append(val)

# printing result
print("The resolved dictionary values : " + str(res))
