# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the description
description = user.description

print("The description of the user is : " + description)
