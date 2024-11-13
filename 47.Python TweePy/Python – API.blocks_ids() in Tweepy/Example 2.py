# getting the blocked users
blocked_users = api.blocks_ids()

# printing the user IDs of the blocked users
for IDs in blocked_users:
	print(IDs)
