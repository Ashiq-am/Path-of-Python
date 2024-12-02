import random
import string

# Generate a random string of 8 unique characters
def generate_random_string(length):
    chars = list(string.ascii_letters)
    random.shuffle(chars)  # Shuffle the list of characters
    return ''.join(chars[:length])


random_string = generate_random_string(8)
print(random_string)