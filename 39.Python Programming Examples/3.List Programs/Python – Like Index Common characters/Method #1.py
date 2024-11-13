# Python3 code to demonstrate
# Like Index Common characters
# using list comprehension + zip() + intersection()

# initializing lists
test_list1 = ["Geeksfor", "is", "be"]
test_list2 = ['Geeks', 'sb', 'ste']

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using list comprehension + zip()
# Like Index Common characters + intersection()
res = ["".join(list(set(i).intersection(set(j)))) for i, j in zip(test_list1, test_list2)]

# printing result
print ("The list after element intersection is : " + str(res))
