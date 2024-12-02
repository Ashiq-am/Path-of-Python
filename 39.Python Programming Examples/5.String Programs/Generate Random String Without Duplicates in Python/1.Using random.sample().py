import random
import string

# Generate a random string of 8 unique characters
def generate_random_string(length):
    return ''.join(random.sample(string.ascii_letters, length))


random_string = generate_random_string(8)
print(random_string)