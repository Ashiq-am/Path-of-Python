# Python3 code to demonstrate working of
# Mathematical Median of Cumulative Records
# Using loop + "~" operator

# initializing list
test_list = [(1, 4, 5), (7, 8), (2, 4, 10)]

# printing list
print("The original list : " + str(test_list))

# Mathematical Median of Cumulative Records
# Using loop + "~" operator
res = []
for sub in test_list :

    for ele in sub :
        res.append(ele)
res.sort()
mid = len(res) // 2
res = (res[mid] + res[~mid]) / 2

# Printing result
print("Median of Records is : " + str(res))
