# Using a Custom Function
def custom_sort(dictionary):
	return dictionary['age']

list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_list = sorted(list_of_dicts, key=custom_sort, reverse=True)

#Display sorted list
print(sorted_list)
