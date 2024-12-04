s1 = input("Enter your password: ")

if 8 <= len(s1) <= 20:
    print("Password length is valid!")
else:
    print("Password must be between 8 and 20 characters.")