# the ID of the non-existent list
list_id = ""

# remove the following users from the list
users = ["geeksforgeeks", "PracticeGfG",
		"GeeksQuiz", "hackerrank"]

print("Number of members before remove_list_member() is used : " +
	str(api.get_list(list_id = list_id).member_count))

# removing the users to the list
api.remove_list_members(list_id = list_id, screen_name = users)

print("Number of members after remove_list_member() is used : " +
	str(api.get_list(list_id = list_id).member_count))
