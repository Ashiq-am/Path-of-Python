import re

# Original string
s = "My phone number is 123-456-7890 and my friend's is 987-654-3210"

# Replace all phone numbers (pattern: digits followed by hyphens)
new_s, count = re.subn(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", s)

print(new_s)
print(count)