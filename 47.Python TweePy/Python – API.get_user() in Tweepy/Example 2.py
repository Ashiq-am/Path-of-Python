# using get_user with user_id
user_id = "57741058"
user = api.get_user(user_id)

# printing the name of the user
print("The user id " + user_id +
	" corresponds to the user with the name : " +
	user.name)

# using get_user with screen_name
screen_name = "geeksforgeeks"
user = api.get_user(screen_name)

# printing the name of the user
print("\nThe screen name " + screen_name +
	" corresponds to the user with the name : " +
	user.name)
