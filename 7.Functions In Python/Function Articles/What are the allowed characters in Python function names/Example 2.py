""


'''

# Python code to demonstrate
# that we can't use special
# character like !,@,#,$,%.etc
# as identifier

# valid identifier
var1 = 46
var2 = 23
print(var1 * var2)

# invalid identifier,
# will give invalid syntax error
var@ = 12
$var = 55
print(var@ * $var)

# even function names can't
# have special characters
def my_function%():
print('This is a function with invalid identifier')

my_function%()


'''