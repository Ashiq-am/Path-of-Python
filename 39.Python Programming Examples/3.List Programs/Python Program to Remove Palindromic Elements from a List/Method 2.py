# initializing list
test_list = [54, 67, 12, 45, 98, 76, 9]

# printing original list
print("The original list is : " + str(test_list))

# reversing and comparing for presence using in operator
res = list(filter(lambda ele: int(str(ele)[::-1]) not in test_list, test_list))

# printing result
print("List after palindromic removals ? : " + str(res))
