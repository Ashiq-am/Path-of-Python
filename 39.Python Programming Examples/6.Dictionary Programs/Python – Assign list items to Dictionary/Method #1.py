# Python3 code to demonstrate working of
# Assign list items to Dictionary
# Using zip() + loop

# initializing list
test_list = [{'Gfg': 1, 'id': 2},
             {'Gfg': 4, 'id': 4}]

# printing original list
print("The original list is : " + str(test_list))

# initializing key
new_key = 'best'

# initializing list
add_list = [12, 2]

# Assign list items to Dictionary
# Using zip() + loop
res = []
for sub, val in zip(test_list, add_list):
    sub[new_key] = val
    res.append(sub)

# printing result
print("The modified dictionary : " + str(res))
