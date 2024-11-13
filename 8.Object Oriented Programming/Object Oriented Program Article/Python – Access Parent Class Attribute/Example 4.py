class Vehicle:

    def __init__(self):
        # instantiating the 'Inner' class
        self.inner = self.Car()

        # instantiating the multilevel
        # 'InnerInner' class
        self.innerinner = self.inner.Maruti()

    def show_classes(self):
        print("This is in Outer class that is Vehicle")

    # inner class
    class Car:
        # First Inner Class

        def __init__(self):
            # instantiating the
            # 'InnerInner' class
            self.innerinner = self.Maruti()

        def show_classes(self):
            print("This is in Inner class that is Car")

        # multilevel inner class
        class Maruti:

            def inner_display(self, msg):
                print("This is in multilevel InnerInner\
					class that is Maruti")
                print(msg)


# Driver Code
outer = Vehicle()
outer.show_classes()
inner = outer.Car()
inner.show_classes()
innerinner = inner.Maruti()

# Calling the method inner_display
innerinner.inner_display("Just Print It!")
