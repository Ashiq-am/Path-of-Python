def find_second_occurrence(main_str, sub_str):
	first_occurrence = main_str.find(sub_str)

	if first_occurrence != -1:
		second_occurrence = main_str.find(sub_str, first_occurrence + 1)
		return second_occurrence if second_occurrence != -1 else "Substring appears only once."
	else:
		return "Specified substring not found."


# Example usage
main_text = "Python is powerful, and Python is versatile."
sub_text = "Python"
result = find_second_occurrence(main_text, sub_text)
print("Index of the second occurrence:", result)
