# Python3 code to demonstrate working of
# Percentage similarity of lists
# using "|" operator + "&" operator + set()

# initialize lists
test_list1 = [1, 4, 6, 8, 9, 10, 7]
test_list2 = [7, 11, 12, 8, 9]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Percentage similarity of lists
# using "|" operator + "&" operator + set()
res = len(set(test_list1) & set(test_list2)) / float(len(set(test_list1) | set(test_list2))) * 100

# printing result
print("Percentage similarity among lists is : " + str(res))
