# Code to demonstrate use
# of __getitem__() in python


class Test(object):

    # This function prints the type
    # of the object passed as well
    # as the object item
    def __getitem__(self, items):
        print(type(items), items)


# Driver code
test = Test()
test[5]
test[5:65:5]
test['GeeksforGeeks']
test[1, 'x', 10.0]
test['a':'z':2]
test[object()]
