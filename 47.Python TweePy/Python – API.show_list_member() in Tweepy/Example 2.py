# the ID of the list
list_id = ""

# the user to be checked in the list
screen_name = "abcxyz"

# checking the user is present in the list or not
api.show_list_member(list_id = list_id, screen_name = screen_name)

# if there is no exception then the user is present
print("The user " + screen_name + " is present in the list.")
