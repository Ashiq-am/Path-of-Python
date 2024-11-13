# program to demonstrate __getslice__ method

class MyClass:
    def __init__(self, string):
        self.string = string

    # method for creating list of words
    def getwords(self):
        return self.string.split()

    # method to perform slicing on the
    # list of words
    def __getslice__(self, i, j):
        return self.getwords()[max(0, i):max(0, j)]


# Driver Code
if __name__ == '__main__':
    # object creation
    obj = MyClass("Hello World ABC")

    # __getslice__ method called internally
    # from the class
    sliced = obj[0:2]

    # print the returned output
    # return type is list
    print(sliced)
