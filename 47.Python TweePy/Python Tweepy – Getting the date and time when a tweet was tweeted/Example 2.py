# the ID of the status
id = 1272479136133627905

# fetching the status
user = api.get_status(id)

# fetching the created_at attribute
created_at = status.created_at

print("The status was created at : " + str(created_at))
