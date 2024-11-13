# Python3 code to demonstrate working of
# Records List Concatenation
# using list comprehension + zip()

# initialize lists
test_list1 = [("g", "f"), ("g", "is"), ("be", "st")]
test_list2 = [("fg", "g"), ("gf", "best"), ("st", " gfg")]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Records List Concatenation
# using list comprehension + zip()
res = [(x[0] + y[0], x[1] + y[1]) for x, y in zip(test_list1, test_list2)]

# printing result
print("The Concatenation across lists is : " + str(res))
