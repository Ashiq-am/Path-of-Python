# data
website_name = "GeeksforGeeks"
founded_year = 2009
is_popular = True

# open a file in write mode
with open('output.txt', 'w') as file:
	# write variables using str() function
	file.write("Website Name: " + str(website_name) + '\n')
	file.write("Founded Year: " + str(founded_year) + '\n')
	file.write("Is Popular: " + str(is_popular) + '\n')
