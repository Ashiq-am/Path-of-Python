# the screen name of the owner of the list
owner_screen_name = "Ashiqul Amin"

# the ID of the list
list_id = print("Before using destroy_list() method")
if api.get_list(list_id):
	print("The list exists.")

# deleting the list
api.destroy_list(owner_screen_name, list_id = list_id)

print("After using destroy_list() method")
try:
	api.get_list(list_id)
except:
	print("The list does not exists.")
