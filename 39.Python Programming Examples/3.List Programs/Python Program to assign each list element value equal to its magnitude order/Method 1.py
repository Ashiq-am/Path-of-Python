# Python3 code to demonstrate working of
# Relative Size Ordering
# Using set() + zip() + sorted() + dict() + list comprehension

# initializing list
test_list = [8, 3, 5, 8, 1, 5, 4]

# printing original list
print("The original list is : " + str(test_list))

# assigning order to each value
ord_dict = dict(zip(list(set(test_list)),
                    range(len(set(test_list)))))

# mapping element with ordered value
res = [ord_dict[ele] for ele in test_list]

# printing result
print("Relative size ordered list : " + str(res))
