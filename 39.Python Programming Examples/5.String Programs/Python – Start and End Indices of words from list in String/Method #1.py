# Python3 code to demonstrate working of
# Start and End Indices of words from list in String
# Using loop + index() + len()

# initializing string
test_str = "gfg is best for all CS geeks and engineering job seekers"

# printing original string
print("The original string is : " + str(test_str))

# initializing check_list
check_list = ["geeks", "engineering", "best", "gfg"]

res = dict()
for ele in check_list:
    if ele in test_str:
        # getting front index
        strt = test_str.index(ele)

        # getting ending index
        res[ele] = [strt, strt + len(ele) - 1]

# printing result
print("Required extracted indices : " + str(res))
