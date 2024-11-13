import re

text = "The cat sat on the mat."

pattern = r"(?P<animal>cat)"

replaced_text = re.sub(pattern, r"dog", text)
print(replaced_text)  # Output: The dog sat on the mat.
