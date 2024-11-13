# screen name of the user
screen_name = "geeksforgeeks"

# getting the liked statuses
favorites = api.favorites(screen_name)

# printing the screen names of the status posters
for status in favorites:
	print(status.user.screen_name)
