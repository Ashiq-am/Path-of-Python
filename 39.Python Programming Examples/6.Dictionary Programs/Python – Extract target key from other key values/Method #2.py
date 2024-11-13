# Python3 code to demonstrate working of
# Extract target key from other key values
# Using loop + conditions ( for multiple / unknown keys )

def hlper_func(test_keys, filt_key):
    for key in test_keys.keys():
        if key in filt_key:
            if test_keys[key] != int(filt_key[key]):
                return False
    return True


# initializing list
test_list = [{'name': 'Manjeet', 'English': 14, 'Maths': 2},
             {'name': 'Akshat', 'English': 7, 'Maths': 13},
             {'name': 'Akash', 'English': 1, 'Maths': 17},
             {'name': 'Nikhil', 'English': 10, 'Maths': 18}]

# printing original list
print("The original list is : " + str(test_list))

# initializing filter items
filt_key = {'English': 7, 'Maths': 13}

# Extract target key from other key values
# Using loop + conditions ( for multiple / unknown keys )
res = []
for sub in test_list:
    if hlper_func(sub, filt_key):
        res.append(sub['name'])

# printing result
print("The filtered result : " + str(res))
