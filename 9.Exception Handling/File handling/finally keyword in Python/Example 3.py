# Python program to demonstrate finally

# Exception is not handled
try:
    k = 5 // 0  # exception raised
    print(k)

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
