# ID of the saved search
id = 1269503225993900032

# fetching the saved search
saved_search = api.get_saved_search(id)

# printing the information
print("The saved search " + str(saved_search.id) +
	" was created on : " + str(saved_search.created_at))
