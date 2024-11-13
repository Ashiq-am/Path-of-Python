# the ID of the status
id = 1272479136133627905

# fetching the status
status = api.get_status(id)

# fetching the favorite_count attribute
favorite_count = status.favorite_count

print("The number of time the status has been favourited is : " + str(favorite_count))
