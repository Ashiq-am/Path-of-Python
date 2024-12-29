class shape:
    def display(self):
        print("class shape")

class circle(shape):
    def display(self):
        print("class circle")

class square(shape):
    def display(self):
        print("class square")

class cylinder(circle, square):
    pass

obj = cylinder()
obj.display()  # Calls circle's display method
