# Python3 code to demonstrate working of
# Decreasing point in List
# Using loop

# initializing list
test_list = [3, 6, 8, 9, 12, 5, 18, 1]

# printing original list
print("The original list is : " + str(test_list))

res = -1
for idx in range(0, len(test_list) - 1):

    # checking for 1st decreasing element
    if test_list[idx + 1] < test_list[idx]:
        res = idx
        break

# printing result
print("Decreasing Point : " + str(res))
