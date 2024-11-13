# Python code to initialize 1D-list

# Initialize using star operator
# list of size 5 will be initialized.
# star is used outside the list.
list1 = [0]*5


# Initialize using list comprehension
# list of size 5 will be initialized.
# range() is used inside list.
list2 = [0 for i in range(5)]

print("list1 : ", list1)
print("list2 : ", list2)
