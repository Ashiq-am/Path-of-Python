# Define a set with programming languages related to GeeksforGeeks
gfg_articles_set = {'Python', 'Java', 'C', 'C++', 'JavaScript', 'Ruby'}

# Initialize an empty list
gfg_articles_list = []

# Convert the set to a list using a loop with append()
for articles in gfg_articles_set:
	gfg_articles_list.append(articles)

# Display the original set and the resulting list
print("Original Set:", gfg_articles_set)
print("Converted List:", gfg_articles_list)
