# Python program to illustrate
# callable()
class Geek:

    def testFunc(self):
        print('Hello GeeksforGeeks')

# Suggests that the Geek class is callable
print(callable(Geek))

GeekObject = Geek()
# The object will be created but
# returns an error on calling
GeekObject()
