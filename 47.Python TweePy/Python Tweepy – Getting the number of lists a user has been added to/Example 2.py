# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the listed_count
listed_count = user.listed_count

print("The number of lists the user has been added to are : " + str(listed_count))
