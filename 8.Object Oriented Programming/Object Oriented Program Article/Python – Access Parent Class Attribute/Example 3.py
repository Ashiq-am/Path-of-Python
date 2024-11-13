class Electronics:
    def __init__(self):
        print('SINGLA ELECTRONICS')
        self.laptop = self.Laptop()
        self.mobile = self.Mobile()

    # Inner Class 1
    class Laptop:
        def operation(self):
            print('DELL Inspiron 15')

    # Inner Class 2
    class Mobile:
        def operation(self):
            print('Redmi Note 5')


# Driver Code
ele = Electronics()
ele.laptop.operation()
ele.mobile.operation()
