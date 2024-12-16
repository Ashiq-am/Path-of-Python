import re

a = "apple orange apple banana"
pattern = "apple"
repl = "grape"

# Replace all occurrences of "apple" with "grape"
result = re.sub(pattern, repl, a)

print(result)