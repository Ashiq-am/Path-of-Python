# Python3 code to demonstrate working of
# Sort Dictionary by Key Lengths
# Using len() + sort() + dictionary comprehension + items()

def get_len(key):
	return len(key[0])

# initializing dictionary
test_dict = {"Gfg" : 4, "is" : 1, "best" : 0, "for" : 3, "geeks" : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# sorting using sort()
# external to render logic
test_dict_list = list(test_dict.items())
test_dict_list.sort(key = get_len)

# reordering to dictionary
res = {ele[0] : ele[1] for ele in test_dict_list}

# printing result
print("The sorted dictionary : " + str(res))
