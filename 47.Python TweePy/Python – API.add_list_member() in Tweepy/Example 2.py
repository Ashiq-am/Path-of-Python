# the ID of the non-existent list
list_id = ''

# add the following users to the list
users = ["geeksforgeeks", "PracticeGfG",
		"GeeksQuiz", "hackerrank"]

print("Number of members before add_list_member() is used : " +
	str(api.get_list(list_id = list_id).member_count))

# adding the users to the list
for screen_name in users:
	api.add_list_member(list_id = list_id, screen_name = screen_name)

print("Number of members after add_list_member() is used : " +
	str(api.get_list(list_id = list_id).member_count))
