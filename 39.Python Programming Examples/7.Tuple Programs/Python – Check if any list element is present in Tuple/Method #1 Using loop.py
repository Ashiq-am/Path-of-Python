# Python3 code to demonstrate working of
# Check if any list element is present in Tuple
# Using loop

# initializing tuple
test_tup = (4, 5, 7, 9, 3)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing list
check_list = [6, 7, 10, 11]

res = False
for ele in check_list:

    # checking using in operator
    if ele in test_tup:
        res = True
        break

# printing result
print("Is any list element present in tuple ? : " + str(res))
