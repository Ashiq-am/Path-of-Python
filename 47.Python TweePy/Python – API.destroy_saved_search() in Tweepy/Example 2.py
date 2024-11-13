# fetching all the saved searhces
saved_searches = api.saved_searches()

print("The number of saved searches before destroy_saved_search() : ", end = "")
print(len(saved_searches))

# deleting all the saved search
for saved_search in saved_searches:
	api.destroy_saved_search(saved_search.id)

print("The number of saved searches after destroy_saved_search() : ", end = "")
print(len(api.saved_searches()))
