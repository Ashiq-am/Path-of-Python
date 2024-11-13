# initializing list
test_list = [[3345, 6355, 83, 938], [
	323, 923, 845], [192, 993, 49], [98, 34, 23]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# checking for all elements match using all()
res = [row for row in test_list if all(
	str(i)[K] == str(row[0])[K] for i in row)]

# printing result
print("Filtered Rows : " + str(res))
