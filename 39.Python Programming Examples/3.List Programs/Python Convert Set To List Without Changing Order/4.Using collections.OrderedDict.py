from collections import OrderedDict

# Define a set with programming languages related to GeeksforGeeks
gfg_articles_set = {'Python', 'Java', 'C', 'C++', 'JavaScript', 'Ruby'}

# Convert the set to a list using collections.OrderedDict
gfg_articles_list = list(OrderedDict.fromkeys(gfg_articles_set))

# Display the original set and the resulting list
print("Original Set:", gfg_articles_set)
print("Converted List:", gfg_articles_list)
