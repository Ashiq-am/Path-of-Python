# Python3 code to demonstrate working of
# Test for alternate peak List
# Using all() + generator expression

# initializing list
test_list = [2, 4, 1, 6, 4, 8, 0]

# printing original list
print("The original list is : " + str(test_list))

# checking for all the elements for alternate peaks
# one liner solution to problem
res = all(((test_list[idx - 1] < test_list[idx]
            and test_list[idx + 1] < test_list[idx])
           or (test_list[idx - 1] > test_list[idx]
               and test_list[idx + 1] > test_list[idx]))
          for idx in range(1, len(test_list) - 1))

# printing result
print("Is list forming alternate peaks ? : " + str(res))
