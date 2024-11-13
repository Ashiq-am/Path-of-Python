# ID of the status
from tweepy import api

id = 1267740427676942337

print("Before using the destroy_favorite() method : ")
if api.get_status(id).favorited == True:
	print("The status has been liked by the authenticated user.")
else:
	print("The status has not been liked by the authenticated user.")

# un-liking the status
api.destroy_favorite(id)

print("\nAfter using the destroy_favorite() method : ")
if api.get_status(id).favorited == True:
	print("The status has been liked by the authenticated user.")
else:
	print("The status has not been liked by the authenticated user.")
