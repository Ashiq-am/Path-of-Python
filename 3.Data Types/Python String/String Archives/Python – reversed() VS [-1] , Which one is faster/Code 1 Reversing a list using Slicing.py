# Python code to reverse
# a list using slicing

ls = [110, 220, 330,
	440, 550]
print('Original list :', ls)

# list reverse
ls = ls[::-1]

print('Reversed list elements :')
for element in ls:
    print(element)
