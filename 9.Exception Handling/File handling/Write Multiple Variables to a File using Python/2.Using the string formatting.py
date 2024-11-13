# data/variables
website_name = "GeeksforGeeks"
founded_year = 2009
is_popular = True

# open a file in write mode
with open('output.txt', 'w') as file:
	# write variables using string formatting
	file.write("Website Name: {}\n".format(website_name))
	file.write("Founded Year: {}\n".format(founded_year))
	file.write("Is Popular: {}\n".format(is_popular))
