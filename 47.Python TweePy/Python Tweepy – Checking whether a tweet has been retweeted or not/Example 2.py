# the ID of the status
id = 1272479136133627905

# fetching the status
status = api.get_status(id)

# fetching the retweeted attribute
retweeted = status.retweeted

if retweeted == True:
	print("The authenticated user has retweeted the tweet.")
else:
	print("The authenticated user has not retweeted the tweet.")
