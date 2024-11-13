# create a Geeksforgeeks class
class Geeksforgeeks:

    # constructor method
    def __init__(self):
        # object attributes
        self.course = "Campus preparation"
        self.duration = "2 months"

    # define a show method
    # for printing the content
    def show(self):
        print("Course:", self.course)
        print("Duration:", self.duration)

# create Geeksforgeeks
# class object
outer = Geeksforgeeks()

# method calling
outer.show()
