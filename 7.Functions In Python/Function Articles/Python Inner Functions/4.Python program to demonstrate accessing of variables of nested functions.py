# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = 'I love GeeksforGeeks'

    def f2():
        s = 'Me too'
        print(s)

    f2()
    print(s)


# Driver's code
f1()
