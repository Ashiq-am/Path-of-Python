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

# iterate over the list
for i in languages:

    # now i is a dict, now we see the keys
    # of the dict
    for key in i.keys():
        # print every key of each dict
        print(key)

    print("-------------")
