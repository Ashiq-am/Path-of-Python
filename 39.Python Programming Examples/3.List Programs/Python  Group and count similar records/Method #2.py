# Python3 code to demonstrate working of
# Group and count similar records
# using Counter() + list comprehension + items()
from collections import Counter

# initialize list
test_list = [('gfg', ), ('is', ), ('best', ), ('gfg', ),
					('is', ), ('for', ), ('geeks', )]

# printing original list
print("The original list : " + str(test_list))

# Group and count similar records
# using Counter() + list comprehension + items()
res = [(counter, ) + ele for ele, counter in Counter(test_list).items()]

# printing result
print("Grouped and counted list is : " + str(res))
