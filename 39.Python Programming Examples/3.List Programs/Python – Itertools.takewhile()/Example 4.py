import random
from itertools import takewhile

# generating alphabets in random order
li = random.sample(range(97, 123), 26)
li = list(map(chr, li))

print("The original list list is :")
print(li)

# consider the element until
# 'e' or 'i' or 'o' is encountered
new_li = list(takewhile(lambda x:x not in ['e', 'i', 'o'],
						li))

print("\nThe new list is :")
print(new_li)
