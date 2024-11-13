# Python3 code to demonstrate working of
# Mixed Combinations of string and list
# using loop + enumerate() + replace()

# initialize list and string
test_list = ["a", "b", "c"]
test_str = "gfg"

# printing original list and string
print("The original list : " + str(test_list))
print("The original string : " + test_str)

# Mixed Combinations of string and list
# using loop + enumerate() + replace()
res = []
for idx, ele in enumerate(test_str):
	res += [test_str[ : idx] + test_str[idx : ].replace(ele, k, 1)
			for k in test_list]

# printing result
print("The list after mixed Combinations : " + str(res))
