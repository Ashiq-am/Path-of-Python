# the screen name user
screen_name = "geeksforgeeks"

# fetching all the lists
api.lists_memberships(screen_name)

# counting the number of lists
print("The user " + screen_name + " has been added to " + str(len(list)) + " list(s).")
