# Python3 code to demonstrate working of
# Elements Maximum till current index in List
# Using max() + list comprehension + list slicing

# initializing list
test_list = [3, 5, 2, 6, 7, 9, 3]

# printing original list
print("The original list : " + str(test_list))

# Using max() + list comprehension + list slicing
# max() used to get if current is current maximum
res = [test_list[idx] for idx in range(
	1, len(test_list)) if test_list[idx] > max(test_list[:idx])]

# printing result
print("Extracted Maximum elements : " + str(res))
