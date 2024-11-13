# ID of the user
id = 4802800777

print("Before using the destroy_block() method : ")
if api.show_friendship(target_id = id)[0].blocking == True:
	print("The user has been blocked by the authenticated user.")
else:
	print("The user has not been blocked by the authenticated user.")

# blocking the user
api.destroy_block(id)

print("\nAfter using the destroy_block() method : ")
if api.show_friendship(target_id = id)[0].blocking == True:
	print("The user has been blocked by the authenticated user.")
else:
	print("The user has not been blocked by the authenticated user.")
