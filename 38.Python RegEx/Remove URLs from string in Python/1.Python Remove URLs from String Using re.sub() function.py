import re
def remove_urls(text, replacement_text="[URL REMOVED]"):
	# Define a regex pattern to match URLs
	url_pattern = re.compile(r'https?://\S+|www\.\S+')

	# Use the sub() method to replace URLs with the specified replacement text
	text_without_urls = url_pattern.sub(replacement_text, text)

	return text_without_urls

# Example:
input_text = "Visit on GeeksforGeeks Website: https://www.geeksforgeeks.org/"
output_text = remove_urls(input_text)

print("Original Text:")
print(input_text)
print("\nText with URLs Removed:")
print(output_text)
