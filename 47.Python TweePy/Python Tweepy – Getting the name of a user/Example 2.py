# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the name
name = user.name

print("The name of the user is : " + name)
