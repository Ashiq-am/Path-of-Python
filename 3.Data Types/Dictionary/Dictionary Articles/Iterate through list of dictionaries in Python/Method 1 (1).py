# Create a list of dictionaries
languages = [
	{
		"Python": "Machine Learning",
		"R": "Machine learning",
	},
	{
		"Python": "Web development",
		"Java Script": "Web Development",
		"HTML": "Web Development"
	},
	{
		"C++": "Game Development",
		"Python": "Game Development"
	},
	{
		"Java": "App Development",
		"Kotlin": "App Development"
	}
]

for key, val in languages[0].items():
	print("{} : {}".format(key, val))
