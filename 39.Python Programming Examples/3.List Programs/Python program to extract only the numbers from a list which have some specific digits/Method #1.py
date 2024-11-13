# Python3 code to demonstrate working of
# Elements with specific digits
# Using list comprehension + all()

# initializing list
test_list = [345, 23, 128, 235, 982]

# printing original list
print("The original list is : " + str(test_list))

# initializing digit list
dig_list = [2, 3, 5, 4]

# checking for all digits using all()
res = [sub for sub in test_list if all(int(ele) in dig_list for ele in str(sub))]

# printing result
print("Extracted elements : " + str(res))
