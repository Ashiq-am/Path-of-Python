# Python3 code to demonstrate working of
# Test if y occurs after x in List
# Using loop + index()

# initializing list
test_list = [4, 5, 6, 2, 4, 5, 2, 9]

# printing original lists
print("The original list is : " + str(test_list))

# initializing x, y
x, y = 6, 2

# getting index of x
xidx = test_list.index(x)

res = True
for idx, ele in enumerate(test_list):

    # checking for y and comparing index
    if ele == y and idx < xidx:
        res = False
        break

# printing result
print("Do all y occur after x : " + str(res))
