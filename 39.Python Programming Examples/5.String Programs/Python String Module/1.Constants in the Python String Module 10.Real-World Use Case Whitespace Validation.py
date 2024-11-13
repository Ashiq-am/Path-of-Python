import string
def is_only_whitespace(s):
    return all(char in string.whitespace for char in s)

print(is_only_whitespace("   \t\n"))
