# Python3 code to demonstrate
# Occurrence counter in List of Records
# using Counter() + loop
from collections import Counter

# Initializing list
test_list = [('Gfg', 1), ('Gfg', 2), ('Gfg', 3), ('Gfg', 1), ('Gfg', 2), ('is', 1), ('is', 2)]

# printing original list
print("The original list is : " + str(test_list))

# Occurrence counter in List of Records
# using Counter() + loop
res = {}
for key, val in test_list:
	res[key] = [val] if key not in res else res[key] + [val]

res = {key: dict(Counter(val)) for key, val in res.items()}

# printing result
print ("Mapped resultant dictionary : " + str(res))
