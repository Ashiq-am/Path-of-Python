import re

# Original string
s = "This is a Test. This is another Test."

# Replace 'test' with 'exam', ignoring case
new_s, count = re.subn(r"test", "exam", s, flags=re.IGNORECASE)

print(new_s)
print("Replacements made:", count)