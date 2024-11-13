# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the create_at attribute
created_at = user.created_at

print("The user was created on : " + str(created_at))
