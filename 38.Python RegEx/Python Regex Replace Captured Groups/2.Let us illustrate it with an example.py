import re

text = "geek mail geek.joe@example.com, and wane's email is wane.smith@example.org"

pattern = r"(\w+\.\w+)@(\w+\.\w+)"

matches = re.findall(pattern, text)
print(matches)
