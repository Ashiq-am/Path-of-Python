class Geeks1:
    def code(self, ide):
        ide.execute()


class Geeks2:
    def execute(self):
        print("GeeksForGeeks is the best Platform for learning")


# create object of Geeks2
ide = Geeks2()

# create object of class Geeks1
G1 = Geeks1()

# calling the function by giving ide as the argument.
G1.code(ide)
