# Python3 code to demonstrate
# the random generation of string id's

import random
import string

# defining function for random
# string id with parameter
def ran_gen(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

# function call for random string
# generation with size 8 and string
print (ran_gen(8, "AEIOSUMA23"))
