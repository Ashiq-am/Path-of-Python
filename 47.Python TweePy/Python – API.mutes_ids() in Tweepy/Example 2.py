# getting the muted users
muted_users = api.mutes_ids()

# printing the user IDs of the muted users
for IDs in muted_users:
	print(IDs)
