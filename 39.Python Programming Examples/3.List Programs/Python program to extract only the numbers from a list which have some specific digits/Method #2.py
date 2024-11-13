# Python3 code to demonstrate working of
# Elements with specific digits
# Using filter() + lambda + all()

# initializing list
test_list = [345, 23, 128, 235, 982]

# printing original list
print("The original list is : " + str(test_list))

# initializing digit list
dig_list = [2, 3, 5, 4]

# filter() used to filter from logic
res = list(filter(lambda sub : all(int(ele) in dig_list for ele in str(sub)), test_list))

# printing result
print("Extracted elements : " + str(res))
