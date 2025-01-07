import re

#Find all dates in YYYY-MM-DD format
text = "The event is on 2024-12-25, and the deadline is 2025-01-15."

# Matches a date in YYYY-MM-DD format
pattern = r'\d{4}-\d{2}-\d{2}'

matches = re.findall(pattern, text)
print(matches)