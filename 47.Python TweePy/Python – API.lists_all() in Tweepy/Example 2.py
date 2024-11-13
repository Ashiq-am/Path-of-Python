# the screen name user
screen_name = "geeksforgeeks"

# fetching all the lists
list = api.lists_all(screen_name)

# counting the number of lists
print("The user " + screen_name + " has " + str(len(list)) + " list(s).")
