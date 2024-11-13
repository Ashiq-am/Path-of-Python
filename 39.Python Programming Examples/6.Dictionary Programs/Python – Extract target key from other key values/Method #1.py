# Python3 code to demonstrate working of
# Extract target key from other key values
# Using loop + condition

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
# Using loop + condition
res = []
for sub in test_list:
    if sub["English"] == filt_key["English"] and sub["Maths"] == filt_key["Maths"]:
        res.append(sub['name'])

# printing result
print("The filtered result : " + str(res))
