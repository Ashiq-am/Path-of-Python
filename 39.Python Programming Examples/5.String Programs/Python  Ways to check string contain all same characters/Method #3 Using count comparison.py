# Python code to demonstrate
# to check whether string contains
# all characters same or not

# Initialising string list
ini_list = ["aaaaaaaaaaa", "aaaaaaabaa"]

# Printing initial string
print("Initial Strings list", ini_list)

# Using String comparison
for i in ini_list:
    if i.count(i[0]) == len(i):
        print("String {} have all characters same".format(i))
    else:
        print("String {} don't have all characters same".format(i))

