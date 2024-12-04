import re

s1 = input("Enter your email address: ")

reg = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

if re.match(reg, s1):
    print("Valid email!")
else:
    print("Invalid email!")