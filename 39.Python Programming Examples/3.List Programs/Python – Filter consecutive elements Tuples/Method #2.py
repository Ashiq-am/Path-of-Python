# Python3 code to demonstrate working of
# Filter consecutive elements Tuples
# Using list comprehension

# hlpr_func
def consec_check(tup):
    for idx in range(len(tup) - 1):

        # returns false if any element is not consec.
        if tup[idx + 1] != tup[idx] + 1:
            return False

    return True


# initializing list
test_list = [(3, 4, 5, 6), (5, 6, 7, 2), (1, 2, 3), (6, 4, 6, 3)]

# printing original list
print("The original list is : " + str(test_list))

# one-liner to solve problem, using list comprehension
res = [sub for sub in test_list if consec_check(sub)]

# printing result
print("The filtered tuples : " + str(res))
