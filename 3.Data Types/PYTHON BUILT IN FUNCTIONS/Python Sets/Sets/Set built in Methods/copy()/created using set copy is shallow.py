# Python program to demonstrate that copy
# created using set copy is shallow
first = {'g', 'e', 'e', 'k', 's'}
second = first.copy()

# before adding
print('before adding: ')
print('first: ',first)
print('second: ', second)

# Adding element to second, first does not
# change.
second.add('f')

# after adding
print('after adding: ')
print('first: ', first)
print('second: ', second)
