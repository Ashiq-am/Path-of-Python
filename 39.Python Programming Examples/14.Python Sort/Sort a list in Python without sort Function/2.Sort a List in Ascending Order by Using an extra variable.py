#Python program to print a list
# without using the sort() function
# using an extra variable

l1=[76,23,45,12,54,9]
print("Original List:", l1)

# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            # temporary variable
            temp = l1[i]
            l1[i] = l1[j]
            l1[j] = temp

# sorted list
print("Sorted List", l1)
