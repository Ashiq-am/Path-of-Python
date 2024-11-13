# Python3 code to demonstrate working of
# Mixed Combinations of string and list
# using list comprehension

# initialize list and string
test_list = ["a", "b", "c"]
test_str = "gfg"

# printing original list and string
print("The original list : " + str(test_list))
print("The original string : " + test_str)

# Mixed Combinations of string and list
# using list comprehension
res = [test_str[ : idx] + ele + test_str[idx + 1 : ]\
	for idx in range(len(test_str)) for ele in test_list]

# printing result
print("The list after mixed Combinations : " + str(res))
