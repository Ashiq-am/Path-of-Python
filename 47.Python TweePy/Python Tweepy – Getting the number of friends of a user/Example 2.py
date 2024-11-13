# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the friends_count
friends_count = user.friends_count

print("The number of friends of the user are : " + str(friends_count))
