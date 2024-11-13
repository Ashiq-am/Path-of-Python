# the ID of the status
id = 1272479136133627905

# fetching the status
status = api.get_status(id)

# fetching the id attribute
id = status.id

print("The ID of the status is : " + str(id))
