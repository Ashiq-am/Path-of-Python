# Using the sorted() Function with a Lambda Function
list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_list = sorted(list_of_dicts, key=lambda x: x['age'], reverse=True)

#Display the soted list of dictionaries
print(sorted_list)
