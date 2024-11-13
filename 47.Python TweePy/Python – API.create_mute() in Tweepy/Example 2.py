# ID of the user
id = 4802800777

print("Before using the create_mute() method : ")
if api.show_friendship(target_id = id)[0].muting == True:
	print("The user has been muted by the authenticated user.")
else:
	print("The user has not been muted by the authenticated user.")

# muting the user
api.create_mute(id)

print("\nAfter using the create_mute() method : ")
if api.show_friendship(target_id = id)[0].muting == True:
	print("The user has been muted by the authenticated user.")
else:
	print("The user has not been muted by the authenticated user.")
