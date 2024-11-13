# the ID of the status
id = 1272479136133627905

# fetching the status
status = api.get_status(id)

# fetching the favorited attribute
favorited = status.favorited

if favorited == True:
	print("The authenticated user has liked the tweet.")
else:
	print("The authenticated user has not liked the tweet.")
