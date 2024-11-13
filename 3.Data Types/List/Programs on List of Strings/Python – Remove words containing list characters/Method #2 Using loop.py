# Python3 code to demonstrate
# Remove words containing list characters
# using loop
from itertools import groupby

# initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# initializing char list
char_list = ['g', 'o']

# printing original list
print ("The original list is : " + str(test_list))

# printing character list
print ("The character list is : " + str(char_list))

# Remove words containing list characters
# using loop
res = []
flag = 1
for ele in test_list:
	for idx in char_list:
		if idx not in ele:
			flag = 1
		else:
			flag = 0
			break
	if(flag == 1):
		res.append(ele)

# printing result
print ("The filtered strings are : " + str(res))
