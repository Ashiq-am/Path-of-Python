# Python3 code to demonstrate
# Replace Substrings from String List
# using replace() + list comprehension

# Initializing list1
test_list1 = ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
test_list2 = [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Replace Substrings from String List
# using replace() + list comprehension
res = [sub.replace(sub2[0], sub2[1]) for sub in test_list1
	for sub2 in test_list2 if sub2[0] in sub]

# printing result
print ("The list after replacement : " + str(res))
