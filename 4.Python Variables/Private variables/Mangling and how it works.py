# Python code to illustrate how mangling works
class Map:
    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)

    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

        # private copy of original geek() method

    __geek = geek


class MapSubclass(Map):

    # provides new signature for geek() but
    # does not break __init__()
    def geek(self, key, value):
        for i in zip(keys, values):
            self.list.append(i)






"""The mangling rules are designed mostly to avoid accidents but it is still possible to access or modify 
a variable that is considered private. 
This can even be useful in special circumstances, such as in the debugger."""