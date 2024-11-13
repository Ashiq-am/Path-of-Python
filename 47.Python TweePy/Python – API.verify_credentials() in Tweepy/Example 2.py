# fetching the verified user
user = api.verify_credentials()

# printing the information
print("The user has " + str(user.followers_count) + " followers.")
print("The user has " + str(user.friends_count) + " friends.")
