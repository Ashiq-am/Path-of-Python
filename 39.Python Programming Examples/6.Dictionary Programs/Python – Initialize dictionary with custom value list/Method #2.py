# Python3 code to demonstrate
# Custom list dictionary initialization
# using fromkeys()

# initialization custom list
cus_list = [4, 6]

# using fromkeys() to construct
new_dict = dict.fromkeys(range(4), cus_list)

# printing result
print("New dictionary with custom list as keys : " + str(new_dict))
