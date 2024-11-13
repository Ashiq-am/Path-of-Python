# getting the authenticated user's information
user = api.me()

# printing the ID of the user
print("The authenticated user's ID is : " + str(user.id))
