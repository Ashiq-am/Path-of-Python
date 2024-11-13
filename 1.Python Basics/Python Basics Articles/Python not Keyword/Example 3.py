# Python code to demonstrait
# 'not' keyword

# Function showing working of not keyword
def geek_Func():
    # 1 Not with False boolean value
    geek_x = not False
    print('Negation of False : ', geek_x)

    # 2 Not with true boolean value
    geek_y = not True
    print('Negation of True : ', geek_y)

    # 3 Not with result of and operation
    geek_and = not (True and False)
    print('Negation of result of And operation : ', geek_and)

    # 4 Not with result of or operation
    geek_or = not (True or False)
    print('Negation of result of or operation : ', geek_or)

    # 5 Not with result of compare operation
    geek_Com = not (5 > 7)
    print('Negation of result of And operation : ', geek_Com)


geek_Func()
