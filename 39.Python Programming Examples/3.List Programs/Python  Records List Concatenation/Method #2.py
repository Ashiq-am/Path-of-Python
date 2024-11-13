# Python3 code to demonstrate working of
# Records List Concatenation
# using join() + zip() + map()

# initialize lists
test_list1 = [("g", "f"), ("g", "is"), ("be", "st")]
test_list2 = [("fg", "g"), ("gf", "best"), ("st", " gfg")]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Records List Concatenation
# using join() + zip() + map()
res = [tuple(map("".join, zip(a, b))) for a, b in zip(test_list1, test_list2)]

# printing result
print("The Concatenation across lists is : " + str(res))
