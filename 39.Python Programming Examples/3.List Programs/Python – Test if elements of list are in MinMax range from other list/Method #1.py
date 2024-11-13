# Python3 code to demonstrate working of
# Min/Max range test from other list
# Using loop + min() + max()

# initializing list
test_list = [5, 6, 3, 7, 8, 10, 9]

# printing original lists
print("The original list is : " + str(test_list))

# initializing range_list
range_list = [4, 7, 9, 6]

res = True
for ele in range_list:

    # flag off list in case of any off range element

    #if ele max(test_list):
    if ele in (test_list):
        res = False
        break

# printing result
print("Are all elements in min/max range? : " + str(res))
