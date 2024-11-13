# Python3 code to demonstrate working of
# Consecutive Division in List
# Using loop + / operator

# utility fnc.
def conc_div(test_list):
    res = test_list[0]
    for idx in range(1, len(test_list)):
        # Consecutive Division
        res /= test_list[idx]
    return res


# initializing list
test_list = [1000, 50, 5, 10, 2]

# printing original list
print("The original list is : " + str(test_list))

# getting conc. Division
res = conc_div(test_list)

# printing result
print("The Consecutive Division quotient : " + str(res))
