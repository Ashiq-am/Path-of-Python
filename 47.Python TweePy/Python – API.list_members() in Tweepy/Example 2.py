# the ID of the list
list_id = ""

# fetching the members
members = api.list_members(list_id = list_id)

# printing the number of members
print(len(members))
