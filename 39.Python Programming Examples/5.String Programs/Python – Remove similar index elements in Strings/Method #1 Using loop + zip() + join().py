# Python3 code to demonstrate working of
# Remove similar index elements in Strings
# Using join() + zip() + loop

# initializing strings
test_str1 = 'geeks'
test_str2 = 'beaks'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# conversion to list for zipping
list1 = list(test_str1)
list2 = list(test_str2)
res1 = []
res2 = []
for ch1, ch2 in zip(list1, list2):

    # check inequalities
    if ch1 != ch2:
        res1.append(ch1)
        res2.append(ch2)

    # conversion to string
res1 = "".join(res1)
res2 = "".join(res2)

# printing result
print("Modified String 1 : " + str(res1))
print("Modified String 2 : " + str(res2))
