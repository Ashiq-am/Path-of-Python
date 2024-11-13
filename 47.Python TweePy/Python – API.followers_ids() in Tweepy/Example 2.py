# user ID of the user
user_id = 1037141442

# getting the followers list
followers = api.followers_ids(user_id)

print(api.get_user(user_id).screen_name + " has " + str(len(followers)) + " followers.")
