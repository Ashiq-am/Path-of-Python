# Python3 code to demonstrate working of
# Fill list characters in String
# Using loop

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing fill list
fill_list = ['g', 's', 'f']

# loop to iterate through string
res = ""
for chr in test_str:

    # checking for presence
    if chr in fill_list:
        temp = chr
    else:
        temp = "_"
    res += temp

# printing result
print("The string after filling values : " + str(res))
