# Using urllib.parse
from urllib.parse import urlparse

def remove_urls_urllib(text, replacement_text="[URL REMOVED]"):
	words = text.split()
	for i, word in enumerate(words):
		parsed_url = urlparse(word)
		if parsed_url.scheme and parsed_url.netloc:
			words[i] = replacement_text
	return ' '.join(words)

# Example:
input_text = "Check out the GeeksforGeeks website at https://www.geeksforgeeks.org/ for programming tutorials."
output_text_urllib = remove_urls_urllib(input_text)

print("Using urllib.parse:")
print("Text with URLs Removed:")
print(output_text_urllib)
