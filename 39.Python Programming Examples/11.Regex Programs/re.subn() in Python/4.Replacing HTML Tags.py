import re

text = "<div>Hello</div> <p>World</p>"

pattern = r"</?\w+>"  # Match HTML tags
replacement = "[TAG]"

modified_text, count = re.subn(pattern, replacement, text)

print(modified_text)
print(count)