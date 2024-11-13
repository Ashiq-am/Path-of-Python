# the ID of the user
id = 4802800777

# fetching the user
user = api.get_user(id)

# fetching the screen name
screen_name = user.screen_name

print("The screen name of the user is : " + screen_name)
