# define a function for checking
# number is even or odd
def even_odd(number):



    if number % 2:
        # since num % 2 is equal to 1
        # which is Truthy Value
        return 'odd number'


    else:

        # since num%2 is equal to 0
        # which is Falsy Value.
        return 'even number'

result1 = even_odd(7)

# prints odd
print(result1)

result2 = even_odd(4)

# prints even
print(result2)
