# getting the blocked users
muted_users = api.mutes()

# printing the screen names of the muted users
for user in muted_users:
	print(user.screen_name)
