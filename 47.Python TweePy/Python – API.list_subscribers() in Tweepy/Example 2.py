# the slug of the list
slug = "thought-leaders"

# the sceen name of the owner of the list
owner_screen_name = "kitson"

# number of subscribers to be fetched
count = 3

# fetching the subscribers
subscribers = api.list_subscribers(slug = slug,
								owner_screen_name = owner_screen_name,
								count = count)

print("The number of subscriers fetched : " + str(len(subscribers)))
