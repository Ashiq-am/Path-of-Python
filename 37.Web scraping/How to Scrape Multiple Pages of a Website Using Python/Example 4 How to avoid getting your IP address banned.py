from time import *
from random import randint

for i in range(0,3):
    # selects random integer in given range


    x = randint(2,5)
    print(x)
    sleep(x)
    print(f'I waited {x} seconds')
