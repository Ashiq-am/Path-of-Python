# the ID of the non-existent list
list_id = ""

# add the following users to the list
users = ["geeksforgeeks", "PracticeGfG",
		"GeeksQuiz", "hackerrank"]

print("Number of members before add_list_member() is used : " +
	str(api.get_list(list_id = list_id).member_count))

# adding the users to the list
api.add_list_members(list_id = list_id, screen_name = users)

print("Number of members after add_list_member() is used : " +
	str(api.get_list(list_id = list_id).member_count))
