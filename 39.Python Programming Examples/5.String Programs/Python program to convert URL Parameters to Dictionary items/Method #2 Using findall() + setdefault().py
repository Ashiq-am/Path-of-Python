import re

# initializing string
test_str = 'gfg=4&is=5&best=yes'

# printing original string
print("The original string is : " + str(test_str))

# getting all params
params = re.findall(r'([^=&]+)=([^=&]+)', test_str)

# assigning keys with values
res = dict()
for key, val in params:
    res.setdefault(key, []).append(val)

# printing result
print("The parsed URL Params : " + str(res))
