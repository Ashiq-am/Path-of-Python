# Create a list of dictionaries
languages = [
	{
		"Python" : "Machine Learning",
		"R" : "Machine learning",
	},
	{
		"Python" : "Web development",
		"Java Script" : "Web Development",
		"HTML" : "Web Development"
	},
	{
		"C++" : "Game Development",
		"Python" : "Game Development"
	},
	{
		"Java" : "App Development",
		"Kotlin" : "App Development"
	}
]

# here we are printing the keys of the dictonary
# by using list comprehension and each key will be
# printed in a new line due to the presence of " sep = "\n" ".
# It will add a new line character to our output.

print(*[key for i in languages for key in i.keys()], sep = "\n")
