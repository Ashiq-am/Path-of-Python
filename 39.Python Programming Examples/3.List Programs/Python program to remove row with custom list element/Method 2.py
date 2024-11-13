# initializing Matrix
test_list = [[5, 3, 1], [7, 8, 9], [1, 10, 22], [12, 18, 21]]

# printing original list
print("The original list is : " + str(test_list))

# initializing custom list
check_list = [3, 10, 19, 29, 20, 15]

# filter() used to perform filtering
# any() checks for any element found from check list
res = list(filter(lambda row: not any(
	el in row for el in check_list), test_list))

# printing result
print("The omitted rows matrix : " + str(res))
