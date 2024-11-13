class course:
	name = "data structures using c++"
	duration_months = 6
	price = 20000
	rating = 5

# creating an object of course
print(course.rating)

# deleting the rating attribute from object
delattr(course, 'rating')

# checking if the rating attribute is there or not
try:
	print(course.rating)
except Exception as e:
	print(e)
