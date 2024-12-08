import re

def validate_email():
    while True:
        email = input("Enter email: ")
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return email
        else:
            print("Invalid email format")

# Example usage
email = validate_email()
print(email)