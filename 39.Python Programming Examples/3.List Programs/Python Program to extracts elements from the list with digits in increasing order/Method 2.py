# initializing list
test_list = [1234, 7373, 3643, 3527, 148]

# printing original list
print("The original list is : " + str(test_list))

# sorting and comparing for equality
res = [ele for ele in test_list if ''.join(sorted(str(ele))) == str(ele)]

# printing result
print("Extracted increasing digits : " + str(res))
