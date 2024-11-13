# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the ID
ID = user.id_str

print("The ID of the user is : " + ID)
