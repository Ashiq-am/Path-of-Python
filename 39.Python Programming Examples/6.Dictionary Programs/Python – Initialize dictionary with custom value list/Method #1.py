# Python3 code to demonstrate
# Custom list dictionary initialization
# using dictionary comprehension

# initialize custom list
cus_list = [4, 6]

# using dictionary comprehension to construct
new_dict = {new_list: cus_list for new_list in range(4)}

# printing result
print("New dictionary with custom list as keys : " + str(new_dict))
