import re

a = "apple orange apple banana"
pattern = "apple"
repl = "grape"

# Replace only the first occurrence of "apple"
result = re.sub(pattern, repl, a, count=1)

print(result)