import random

mylist = ["apple", "banana", "mango"]

print(random.choices(mylist, weights = [10, 1, 1], k = 6))
