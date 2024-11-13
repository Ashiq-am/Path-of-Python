# the query to be searched
q = "geeksforgeeks"

# number of users to be retrieved
count = 3

# search the query
users = api.search_users(q, count)

# print the users retrieved
for user in users:
	print(user.screen_name)
