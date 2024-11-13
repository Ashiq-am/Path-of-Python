# Python3 code to demonstrate
# to get most frequent element
# using naive method

# initializing list
test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4]

# printing original list
print("Original list : " + str(test_list))

# using naive method to
# get most frequent element
max = 0
res = test_list[0]
for i in test_list:
    freq = test_list.count(i)
    if freq > max:
        max = freq
        res = i

    # printing result
print("Most frequent number is : " + str(res))
