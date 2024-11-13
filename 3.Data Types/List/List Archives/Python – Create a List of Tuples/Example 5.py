# create a list with name
name = [['sravan'], ['ojaswi'], ['bobby'],
		['rohith'], ['gnanesh']]

# create list of tuple using above list
# using list comprehension and tuple()
# method
data = [tuple(x) for x in name]

# display data
data
