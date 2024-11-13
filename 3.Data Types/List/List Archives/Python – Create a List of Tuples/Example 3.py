# create a list with name
name = ['sravan', 'ojaswi', 'bobby', 'rohith', 'gnanesh']

# zip the two lists using iter() function
data = [x for x in zip(*[iter(name)])]

# display data
data
