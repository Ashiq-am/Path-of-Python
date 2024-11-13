# Python code to reverse
# a list using reversed()

ls = [110, 220, 330, 440, 550]
print('Original list :', ls)

# list reverse
ls = reversed(ls)
print('Iterator object :', ls)

print('Reversed list elements :')
for element in ls:
    print(element)
