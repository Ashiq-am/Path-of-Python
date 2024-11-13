# Python3 code to demonstrate working of
# All possible space joins in String
# Using loop + join()

# initializing string
test_str = 'Geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# All possible space joins in String
# Using loop + join()
res = []
temp = test_str.split(' ')
strt_idx = 0
lst_idx = len(temp)
for idx in range(len(temp) - 1):
    frst_wrd = "".join(temp[strt_idx: idx + 1])
    scnd_wrd = "".join(temp[idx + 1: lst_idx])
    res.append(frst_wrd + " " + scnd_wrd)

# printing result
print("All possible spaces List : " + str(res))
