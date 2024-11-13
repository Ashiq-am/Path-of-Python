# Recursive function for getting length
def list_size(my_list):
	if not my_list:
		return 0
	my_list.pop()
	return 1 + list_size(my_list)


# List in Python
my_list = [32, 89.0, 456, 23, 78, "Lokesh", "Bhopal"]
count = list_size(my_list)
print("The length of the list is : ", count)
