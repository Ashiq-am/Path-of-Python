# the ID of the status
id = 1273112322773581824

# fetching the status
status = api.get_status(id)

# fetching the source attribute
source = status.source

print("The source of the status is : " + source)
