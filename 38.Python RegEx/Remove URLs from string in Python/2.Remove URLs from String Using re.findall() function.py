import re
def remove_urls_findall(text, replacement_text="[URL REMOVED]"):
	url_pattern = re.compile(r'https?://\S+|www\.\S+')
	urls = url_pattern.findall(text)

	for url in urls:
		text = text.replace(url, replacement_text)

	return text

# Example:
input_text = "Check out the latest Python tutorials on GeeksforGeeks: https://www.geeksforgeeks.org/category/python/"
output_text_findall = remove_urls_findall(input_text)

print("\nUsing re.findall():")
print("Original Text:")
print(input_text)
print("\nText with URLs Removed:")
print(output_text_findall)
