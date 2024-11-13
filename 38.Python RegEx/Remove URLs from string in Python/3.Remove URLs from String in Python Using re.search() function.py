import re
def remove_urls_search(text, replacement_text="[URL REMOVED]"):
	url_pattern = re.compile(r'https?://\S+|www\.\S+')

	while True:
		match = url_pattern.search(text)
		if not match:
			break
		text = text[:match.start()] + replacement_text + text[match.end():]

	return text

# Example:
input_text = "Visit our website at https://geeksforgeeks.org/ for more information. Follow us on Twitter: @geeksforgeeks"
output_text_search = remove_urls_search(input_text)

print("\nUsing re.search():")
print("Original Text:")
print(input_text)
print("\nText with URLs Removed:")
print(output_text_search)
