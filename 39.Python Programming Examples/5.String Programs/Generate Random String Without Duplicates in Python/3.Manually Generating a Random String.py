import random
import string


# Generate a random string of 8 unique characters
def generate_random_string(length):
    chars = string.ascii_letters
    result = []

    while len(result) < length:
        char = random.choice(chars)
        if char not in result:
            result.append(char)

    return ''.join(result)


random_string = generate_random_string(8)
print(random_string)