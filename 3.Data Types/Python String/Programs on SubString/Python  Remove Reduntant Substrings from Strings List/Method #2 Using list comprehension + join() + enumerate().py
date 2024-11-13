# Python3 code to demonstrate working of
# Remove Reduntant Substrings from Strings List
# Using list comprehension + join() + enumerate()

# initializing list
test_list = ["Gfg", "Gfg is best", "Geeks", "Gfg is for Geeks"]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension to iterate for each string
# and peform join in one liner
test_list.sort(key = len)
res = [val for idx, val in enumerate(test_list) if val not in ', '.join(test_list[idx + 1:])]

# printing result
print("The filtered list : " + str(res))
