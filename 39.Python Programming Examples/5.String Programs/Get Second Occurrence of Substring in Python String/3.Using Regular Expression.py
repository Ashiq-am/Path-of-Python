import re

def find_second_occurrence_regex(main_str, sub_str):
	matches = [match.start() for match in re.finditer(sub_str, main_str)]

	if len(matches) > 1:
		return matches[1]
	else:
		return "Either the substring appears only once or not at all."

# Example usage
main_text = "Python is powerful, and Python is versatile."
sub_text = "Python"
result_regex = find_second_occurrence_regex(main_text, sub_text)
print("Index of the second occurrence:", result_regex)
