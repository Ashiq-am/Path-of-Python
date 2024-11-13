import string

def is_digit_only(s):
    return all(char in string.digits for char in s)

print("12345 is only digit?", is_digit_only("12345"))
print("123a5 is only digit?", is_digit_only("123a5"))
