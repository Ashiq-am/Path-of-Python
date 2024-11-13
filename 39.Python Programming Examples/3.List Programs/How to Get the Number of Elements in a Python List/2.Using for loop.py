# Python Program for returning the number
# of elements in the list using for loop

list = []  # declaring empty list

# inserting elements in the list using
# append method
list.append(1)
list.append(2)
list.append(3)
list.append(4)

# declaring count variable as integer to keeep
# track of the number of elements in for loop
count = 0

# for loop for iterating through each element
# in the list
for i in list:
    # increments count variable for each
    # iteration
    count = count + 1

# prints the count variable i.e the total number
# of elements in the list
print(list)

print("No of elements in the list are")
print(count)
