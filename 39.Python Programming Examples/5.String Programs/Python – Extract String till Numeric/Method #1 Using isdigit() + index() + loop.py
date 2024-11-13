# Python3 code to demonstrate working of
# Extract String till Numeric
# Using isdigit() + index() + loop

# initializing string
test_str = "geeks4geeks is best"

# printing original string
print("The original string is : " + str(test_str))

# loop to iterating characters
temp = 0
for chr in test_str:

    # checking if character is numeric,
    # saving index
    if chr.isdigit():
        temp = test_str.index(chr)

# printing result
print("Extracted String : " + str(test_str[0: temp]))
