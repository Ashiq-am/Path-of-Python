import re

string = "The quick brown fox jumps over the lazy dog"
pattern = "the"
matches = re.findall(pattern, string)
print(matches)
