s = "hello world"

# Find index of first occurrence of 'o' in string
idx = s.find("o")

# Check if 'o' was found (index is not -1)
if idx != -1:
    # Create a new string by removing first occurrence of 'o'
    s = s[:idx] + s[idx + 1:]

print(s)