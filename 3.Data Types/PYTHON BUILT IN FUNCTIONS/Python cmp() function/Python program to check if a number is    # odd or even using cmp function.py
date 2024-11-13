# Python program to check if a number is
# odd or even using cmp function

# check 12
from filecmp import cmp

n = 12
if cmp(0, n % 2):
    print("odd")
else:
    print("even")

# check 13
n = 13
if cmp(0, n % 2):
    print("odd")
else:
    print("even")
