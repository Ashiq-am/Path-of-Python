# Python code to demonstrate
# to check whether string contains
# all characters same or not

# Initialising string list
ini_list = ["aaaaaaaaaaa", "aaaaaaabaa"]

# Printing initial string
print("Initial Strings list", ini_list)

# Using Naive Method:
flag = True
for i in ini_list:
    for j in range(0, len(i) - 1):
        if i[j] != i[j + 1]:
            print("String {} don't have all characters same".format(i))
            flag = False
            break
    if flag == True:
        print("String {} don't have all characters same".format(i))

