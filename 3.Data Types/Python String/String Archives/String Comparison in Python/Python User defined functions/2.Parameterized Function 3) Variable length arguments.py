# Python program to illustrate
# *args and **kwargs
def myFun1(*argv):
    for arg in argv:
        print(arg)


def myFun2(**kwargs):
    for key, value in kwargs.items():
        print("% s == % s" % (key, value))

    # Driver code


print("Result of * args: ")
myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print("\nResult of **kwargs")
myFun2(first='Geeks', mid='for', last='Geeks')
