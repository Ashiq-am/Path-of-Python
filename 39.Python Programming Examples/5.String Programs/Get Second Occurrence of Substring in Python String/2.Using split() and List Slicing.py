def find_second_occurrence_index_v2(main_str, sub_str):
	try:
		first_occurrence = main_str.index(sub_str)
		second_occurrence = main_str.index(sub_str, first_occurrence + 1)
		return second_occurrence
	except ValueError:
		return "Substring appears only once or not at all."

# Example usage
main_text = "Python is powerful, and Python is versatile."
sub_text = "Python"
result_index_v2 = find_second_occurrence_index_v2(main_text, sub_text)
print("Index of the second occurrence:", result_index_v2)
