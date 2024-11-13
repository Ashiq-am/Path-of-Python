# initializing list
test_list = ["Geeksforgeeks", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing characters list
char_list = ['e', 't', 's', 'm', 'n']

# initializing K
K = 2

# sum() computes matching elements frequency
res = [ele for ele in test_list if sum(ch in char_list for ch in ele) >= K]

# printing result
print("Filtered Strings : " + str(res))
