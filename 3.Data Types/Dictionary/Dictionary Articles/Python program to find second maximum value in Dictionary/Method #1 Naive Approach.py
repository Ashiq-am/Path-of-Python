# Python naive approach to find the
# second largest element in a dictionary

# creating a new dictionary
new_dict ={"google":12, "amazon":9, "flipkart":4, "gfg":13}

# maximum value
max = max(new_dict.values())

# iterate through the dictionary
max2 = 0
for v in new_dict.values():
	if(v>max2 and v<max):
			max2 = v

# print the second largest value
print(max2)
