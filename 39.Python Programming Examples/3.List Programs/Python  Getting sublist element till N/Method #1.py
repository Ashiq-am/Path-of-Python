# Python3 code to demonstrate
# getting sublist element till N
# using list comprehension + list slicing

# initializing list
test_list = [['Geeks', 1, 15], ['for', 3, 5], ['Geeks', 3, 7]]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 2

# using list comprehension + list slicing
# getting sublist element till N
res = [i[0] for i in test_list[ : N]]

# print result
print("The first element of sublist till N : " + str(res))
