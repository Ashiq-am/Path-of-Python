# Python3 code to demonstrate
# to initialize dictionary with list
# using dictionary comprehension

# using dictionary comprehension to construct
new_dict = {new_list: [] for new_list in range(4)}

# printing result
print("New dictionary with empty lists as keys : " + str(new_dict))
