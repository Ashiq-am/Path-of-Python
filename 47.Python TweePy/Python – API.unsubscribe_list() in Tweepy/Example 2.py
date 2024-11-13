# the ID of the list
list_id = 4343

# the slug of the list
slug = "thought-leaders"

# the sceen name of the owner of the list
owner_screen_name = "kitson"

# number of subscribers before unsubscribe_list() method
print("The number of subscribers before unsubscribe_list() method : " +
	str(api.get_list(list_id = list_id).subscriber_count))

# unsubscribing to the list
api.unsubscribe_list(slug = slug, owner_screen_name = owner_screen_name)

# number of subscribers after unsubscribe_list() method
print("The number of subscribers after unsubscribe_list() method : " +
	str(api.get_list(list_id = list_id).subscriber_count))
