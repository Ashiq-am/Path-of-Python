# Python example to demonstrate most_elements() on
# Counter
from collections import Counter

coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219)

# This prints 3 most frequent characters
for letter, count in coun.most_common(3):
	print('%s: %d' % (letter, count))
