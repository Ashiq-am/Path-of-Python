# data
website_name = "GeeksforGeeks"
founded_year = 2009
is_popular = True

# open a file in write mode
with open('output.txt', 'w') as file:
	# write variables using repr() function
	file.write("website_name = " + repr(website_name) + '\n')
	file.write("founded_year = " + repr(founded_year) + '\n')
	file.write("is_popular = " + repr(is_popular) + '\n')
