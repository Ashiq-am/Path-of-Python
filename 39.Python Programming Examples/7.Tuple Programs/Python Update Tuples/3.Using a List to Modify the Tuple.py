# Original tuple
tup1 = (1, 2, 3, 4)

# Convert tuple to list
li = list(tup1)

# Modify the list
li.append(5)  # Adding an element
li[1] = 'a'   # Changing an element

# Convert list back to tuple
tup2 = tuple(li)
print(tup2)