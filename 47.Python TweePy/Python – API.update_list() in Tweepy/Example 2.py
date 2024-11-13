# the screen name of the owner of the list
owner_screen_name = ""

# the ID of the list
list_id = print("Before using update_list() method")
print("The description of the list is : " + api.get_list(list_id = list_id).description)

# the new description of the list
new_description = "This list is to test the Twitter API."

# updating the list
api.update_list(list_id, description = new_description)

print("After using update_list() method")
print("The description of the list is : " + api.get_list(list_id = list_id).description)
