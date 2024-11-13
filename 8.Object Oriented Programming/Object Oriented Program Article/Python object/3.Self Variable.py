class Test:


    def __init__(Myobject, a, b):
        Myobject.country = a
        Myobject.capital = b


    def myfunc(abc):
        print("Capital of " + abc.country +" is:"+abc.capital)

x = Test("India", "Delhi")
x.myfunc()
