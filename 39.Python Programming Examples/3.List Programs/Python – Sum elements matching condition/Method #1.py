# Python 3 code to demonstrate
# Sum elements matching condition
# using loop

# initializing list
test_list = [3, 5, 1, 6, 7, 9]

# printing original list
print("The original list is : " + str(test_list))

# using loop
# Sum elements matching condition
# checks for odd
res = 0
for ele in test_list:
    if ele % 2 != 0:
        res = res + ele

# printing result
print("The sum of odd elements: " + str(res))
