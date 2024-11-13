# Python3 code to demonstrate
# the random generation of id's
# which are multilpe of 5

import random

# determines how many
# values will be printed
for x in range(10):
    # print 10 random values between
    # 1 and 100 which are multiple of 5
    print(random.randint(1, 20) * 5)
