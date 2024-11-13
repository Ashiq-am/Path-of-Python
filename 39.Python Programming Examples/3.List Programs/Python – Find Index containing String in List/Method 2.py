# create a list of names and marks
list1 = ['sravan', 98, 'harsha', 'jyothika',
		'deepika', 78, 90, 'ramya']

# display
list1

# list comprehension
print([list1.index(i) for i in list1 if(type(i) is str)])

# list comprehension display strings
print([i for i in list1 if(type(i) is str)])
