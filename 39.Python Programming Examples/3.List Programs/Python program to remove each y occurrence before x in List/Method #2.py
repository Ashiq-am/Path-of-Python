# Python3 code to demonstrate working of
# Remove each y occurrence before x in List
# Using loop + index()

# initializing list
test_list = [4, 5, 7, 4, 6, 7, 4, 9, 1, 4]

# printing original lists
print("The original list is : " + str(test_list))

# initializing x and y
x, y = 6, 4

# getting index using index()
xidx = test_list.index(x)

# filtering using comparison operators
res = []
for idx, ele in enumerate(test_list):
    if ele != y or (ele == y and idx > xidx):
        res.append(ele)

# printing result
print("Filtered List " + str(res))
