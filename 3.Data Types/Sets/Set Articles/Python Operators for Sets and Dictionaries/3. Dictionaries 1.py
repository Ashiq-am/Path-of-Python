dict = {'math': 45, 'english': 60, 'science': 65,
		'computer science': 70}

# retrieving value by using key
x = dict['science']
print(x)

# reassigning value
dict['english'] = 80
print(dict)

# deleting
del dict['math']
print(dict)
