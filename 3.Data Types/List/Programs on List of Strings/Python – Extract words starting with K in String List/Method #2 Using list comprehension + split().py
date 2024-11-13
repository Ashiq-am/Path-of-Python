# Python3 code to demonstrate working of
# Extract words starting with K in String List
# Using list comprehension + split()

# initializing list
test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = "g"
res = [ele for temp in test_list for ele in temp.split() if ele[0].lower() == K.lower()]

# printing result
print("The filtered elements : " + str(res))
