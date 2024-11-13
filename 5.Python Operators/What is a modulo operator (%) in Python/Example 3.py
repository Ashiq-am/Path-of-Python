# inputs
a = 14
b = 0

# exception handling
try:
    print(a, 'mod', b, '=',
          a % b, sep=" ")

except ZeroDivisionError as err:
    print('Cannot divide by zero!' +
          'Change the value of the right operand.')
