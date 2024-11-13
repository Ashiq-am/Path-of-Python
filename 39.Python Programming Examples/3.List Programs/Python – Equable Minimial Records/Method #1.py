# Python3 code to demonstrate working of
# Equable Minimial Records
# Using min() + list comprehension + lambda

# initializing list
test_list = [('Gfg', 12, 5), ('is', 13, 6), ('best', 12, 2), ('CS', 13, 2)]

# printing original list
print("The original list is : " + str(test_list))

# initializing Equate index
eq_idx = 2

# initializing min index
min_idx = 3

# Equable Minimial Records
# Using min() + list comprehension + lambda
res = [min((ele for ele in test_list if ele[eq_idx - 1] == sub),
           key=lambda a: int(a[min_idx - 1]))
       for sub in {b[eq_idx - 1] for b in test_list}]

# printing result
print("Equable Minimal Records : " + str(res))
