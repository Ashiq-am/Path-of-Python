# getting the blocked users
blocked_users = api.blocks()

# printing the screen names of the blocked users
for user in blocked_users:
	print(user.screen_name)
