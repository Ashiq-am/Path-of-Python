# list of user IDs
user_ids = [813286,
			27260086,
			21447363,
			79293791,
			17919972]

# getting the friendship details
friendships = api.lookup_friendships(user_ids = user_ids)

for friendship in friendships:
	print("Is the authenticated user following " + friendship.screen_name, end = "? : ")
	print(friendship.is_following)
