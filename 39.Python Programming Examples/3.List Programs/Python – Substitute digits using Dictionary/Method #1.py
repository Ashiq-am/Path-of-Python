# Python3 code to demonstrate working of
# Substitute digits using Dictionary
# Using loop

# initializing list
test_list = [45, 32, 87, 34, 21, 91]

# printing original list
print("The original list is : " + str(test_list))

# initializing digit mapping
dig_map = {1 : 4, 4 : 2, 3 : 8, 2 : 6, 7 : 5, 9 : 3, 8 : 9, 5 : 7}

# Substitute digits using Dictionary
# Using loop
temp = []
for idx, ele in enumerate(test_list):
	sub1 = str(ele)
	if len(sub1) > 1:
		sub2 = ""
		for j in sub1:
			if int(j) in dig_map:
				sub2 += str(dig_map[int(j)])
				test_list[idx] = int(sub2)
	else:
		if ele in dig_map:
			test_list[idx] = dig_map[ele]

# printing result
print("List after Digit Substitution : " + str(test_list))
