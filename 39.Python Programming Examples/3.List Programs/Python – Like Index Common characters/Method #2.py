# Python code to demonstrate
# Like Index Common characters
# using map() + lambda + zip() + intersection()

# initializing lists
test_list1 = ["Geeksfor", "is", "be"]
test_list2 = ['Geeks', 'sb', 'ste']

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using map() + lambda + zip() + intersection()
# Like Index Common characters
res = list(map(lambda i, j: "".join(list(set(i).intersection(set(j)))), zip(test_list1, test_list2)))

# printing result
print ("The list after element intersection is : " + str(res))
