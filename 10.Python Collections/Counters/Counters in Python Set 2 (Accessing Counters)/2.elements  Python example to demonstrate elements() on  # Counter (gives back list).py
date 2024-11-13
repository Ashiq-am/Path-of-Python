# Python example to demonstrate elements() on
# Counter (gives back list)
from collections import Counter

coun = Counter(a=1, b=2, c=3)
print(coun)

print(list(coun.elements()))
