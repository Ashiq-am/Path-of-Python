# the ID of the list
list_id = 4343

# screen name of the user to be checked
screen_name = "geeksforgeeks"

# checking if the user is subscribed to the list
api.show_list_subscriber(list_id = list_id, screen_name = screen_name)

# if no exception is raised then the user is subscribed to the list
print("The user " + screen_name + " is subscribed to the list " +
	api.get_list(list_id = list_id).name)
