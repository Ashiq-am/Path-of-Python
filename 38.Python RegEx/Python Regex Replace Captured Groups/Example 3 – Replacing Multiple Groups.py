import re

date_text = "Today's date is 02-09-2024 and yesterday was 01-09-2024."

date_pattern = r"(\d{2})-(\d{2})-(\d{4})"

reformatted_text = re.sub(date_pattern, r"\3-\2-\1", date_text)

print(reformatted_text)
# Output: Today's date is 2024-09-02 and yesterday was 2024-09-01.
