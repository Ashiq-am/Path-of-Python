class sample():

    def myFunc2(x):
        print("I am", x, "from the static method")


sample.myFunc2 = staticmethod(sample.myFunc2)
sample.myFunc2("A")
