# Python3 code to demonstrate working of
# Group and count similar records
# using Counter() + loop + set()
from collections import Counter

# initialize list
test_list = [('gfg', ), ('is', ), ('best', ), ('gfg', ),
					('is', ), ('for', ), ('geeks', )]

# printing original list
print("The original list : " + str(test_list))

# Group and count similar records
# using Counter() + loop + set()
res = []
temp = set()
counter = Counter(test_list)
for sub in test_list:
	if sub not in temp:
		res.append((counter[sub], ) + sub)
		temp.add(sub)

# printing result
print("Grouped and counted list is : " + str(res))
