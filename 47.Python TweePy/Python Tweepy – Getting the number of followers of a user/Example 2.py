# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the followers_count
followers_count = user.followers_count

print("The number of followers of the user are : " + str(followers_count))
