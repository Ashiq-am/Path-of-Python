# Python3 code to demonstrate working of
# Charatacter indices Mapping in String List
# Using enumerate() + dictionary comprehension

# initializing list
test_list = ['g f g', 'i s', 'b e s t', 'f o r', 'g e e k s']

# printing original list
print("The original list is : " + str(test_list))

# using dictionary comprehension to bind result
res = {sub : [key + 1 for key, val in enumerate(test_list) if sub in val]
	for ele in test_list for sub in ele.split()}

# printing result
print("The mapped dictionary : " + str(res))
