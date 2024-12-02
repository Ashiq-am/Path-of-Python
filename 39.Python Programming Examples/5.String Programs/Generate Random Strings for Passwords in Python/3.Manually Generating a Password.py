import random
import string

# Generate a random password of length 10
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []

    while len(password) < length:
        char = random.choice(characters)
        password.append(char)

    return ''.join(password)


password = generate_password(10)
print(password)