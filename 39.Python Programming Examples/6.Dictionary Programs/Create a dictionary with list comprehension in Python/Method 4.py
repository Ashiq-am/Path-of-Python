# creete a list comphrension with student age
data = [('sravan', 23), ('ojaswi', 15),
		('rohith', 8), ('gnanesh', 4), ('bobby', 20)]


# create a dictionary with list
# comprehension if value is equal to 20
print({key: value for (key, value) in data if value == 20})

# create a dictionary with list
# comprehension if value is greater than to 10
print({key: value for (key, value) in data if value > 10})

# create a dictionary with list
# comprehension if key is sravan
print({key: value for (key, value) in data if key == 'sravan'})
