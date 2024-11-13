# initializing list
test_list = [(1, 6), (11, 3), (9, 1), (6, 11), (2, 10), (5, 7)]

# printing original list
print("The original list is : " + str(test_list))

# getting differences pairs
diff_list = [abs(x - y) for x, y in test_list]

# sorting list by computed differences
res = sorted(test_list, key = lambda sub: diff_list.count(abs(sub[0] - sub[1])))

# printing result
print("Sorted Tuples : " + str(res))
