# the name of the list
name = "tweepy_list"

# the description of the list
description = "A Tweepy list"

# the mode of the list
mode = "private"

# creating the list
list = api.create_list(name, description = description, mode = mode)

print("Name of the list : " + list.name)
print("The description of the list : " + str(list.description))
print("Mode of the list : " + list.mode)
