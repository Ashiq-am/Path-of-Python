# creete a list comphrension with student age
data = [('sravan', 23), ('ojaswi', 15),
		('rohith', 8), ('gnanesh', 4), ('bobby', 20)]

# using dict method inside for loop
dict([(key, value) for key, value in data])
