# Python3 code to demonstrate
# Double List
# using loop

# Initializing list
test_list = [12, 67, 98, 34, 43]

# printing original list
print("The original list is : " + str(test_list))

# Double List
# using loop
res = []
for ele in test_list:
    res.append(ele + ele)

# printing result
print("Double List is : " + str(res))
