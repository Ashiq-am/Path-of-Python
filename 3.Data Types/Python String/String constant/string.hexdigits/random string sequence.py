# Importing random to generate
# random string sequence
import random

# Importing string library function
import string


def rand_pass(size):
    # Takes random choices from
    # string.hexdigits
    generate_pass = ''.join([random.choice(string.hexdigits)
                             for n in range(size)])

    return generate_pass


# Driver Code
password = rand_pass(10)
print(password)
