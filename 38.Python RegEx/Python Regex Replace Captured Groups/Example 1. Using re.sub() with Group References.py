import re

# Simple group reference
text = "The cat sat on the mat."

pattern = r"(cat)"

replaced_text = re.sub(pattern, r"dog", text)
print(replaced_text)  # Output: The dog sat on the mat.
