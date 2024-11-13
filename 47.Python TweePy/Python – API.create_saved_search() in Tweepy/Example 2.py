# query of the new saved search
query = "News"

# creating the saved search
saved_search = api.create_saved_search(query)

# printing the information
print("The saved search " + str(saved_search.id) +
	" was created on : " + str(saved_search.created_at))
print("The query of the saved search is : " + saved_search.query)
