class course:
	name = "data structures using c++"
	duration_months = 6
	price = 20000
	rating = 5


# creating an object of course
print(course.price)

# deleting the price attribute from object
delattr(course, 'price')

# checking if the price attribute is there or not
try:
	print(course.price)
except Exception as e:
	print(e)
