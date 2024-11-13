# Python3 code to demonstrate working of
# Remove List elements containing String character
# Using list comprehension

def check_pres(sub, test_str):
    for ele in sub:
        if ele in test_str:
            return 0
    return 1


# initializing list
test_list = ['567', '840', '649', '7342']

# initializing string
test_str = '1237'

# printing original list
print("The original list is : " + str(test_list))

# Remove List elements containing String character
# Using list comprehension
res = [ele for ele in test_list if check_pres(ele, test_str)]

# printing result
print("The list after removal : " + str(res))
