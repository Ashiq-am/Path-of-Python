# Python3 code to demonstrate working of
# Characters Positions Summation in String List
# Using ord() + loop

# initializing list
test_list = ["geeksforgeeks",
             "teaches", "us", "discipline"]

# printing original list
print("The original list is : " + str(test_list))

res = []
for sub in test_list:
    ascii_sum = 0

    # getting ascii value sum
    for ele in sub:
        ascii_sum += (ord(ele) - 96)

    res.append(ascii_sum)

# printing result
print("Position Summation List : " + str(res))
