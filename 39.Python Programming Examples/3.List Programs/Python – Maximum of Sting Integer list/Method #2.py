# Python3 code to demonstrate working of
# Maximum of Sting Integer
# using max() + int() + list comprehension

# initialize list
test_list = [['1', '4'], ['5', '6'], ['7', '10']]

# printing original list
print("The original list : " + str(test_list))

# Maximum of Sting Integer
# using max() + int() + list comprehension
res = [max(int(ele) for ele in sub) for sub in test_list]

# printing result
print("List after maximization of nested string lists : " + str(res))
