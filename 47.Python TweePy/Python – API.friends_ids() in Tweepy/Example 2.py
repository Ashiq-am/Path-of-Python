# user ID of the user
user_id = 145125358

# getting the friends list
friends = api.friends_ids(user_id)

print(api.get_user(user_id).screen_name + " has " + str(len(friends)) + " friends.")
