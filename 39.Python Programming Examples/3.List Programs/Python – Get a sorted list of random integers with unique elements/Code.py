# Python program to create
# a sorted list of unique random
# numbers


import random


# Function to generate a sorted list
# of random numbers in a given
# range with unique elements
def createRandomSortedList(num, start=1, end=100):
    arr = []
    tmp = random.randint(start, end)

    for x in range(num):

        while tmp in arr:
            tmp = random.randint(start, end)

        arr.append(tmp)

    arr.sort()

    return arr


# Driver's code
print(createRandomSortedList(10, 100, 200))
print(createRandomSortedList(5))
