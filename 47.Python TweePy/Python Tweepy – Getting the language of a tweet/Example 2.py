# the ID of the status
id = 1273220141417816064

# fetching the status
status = api.get_status(id)

# fetching the lang attribute
lang = status.lang

print("The language of the status is : " + lang)
