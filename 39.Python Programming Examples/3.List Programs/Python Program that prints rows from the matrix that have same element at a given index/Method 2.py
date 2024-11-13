# initializing list
test_list = [[3345, 6355, 83, 938], [
	323, 923, 845], [192, 993, 49], [98, 34, 23]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# checking for all elements match using all()
# filter() and lambda function performing filtering
res = list(filter(lambda row: all(
	str(i)[K] == str(row[0])[K] for i in row), test_list))

# printing result
print("Filtered Rows : " + str(res))
