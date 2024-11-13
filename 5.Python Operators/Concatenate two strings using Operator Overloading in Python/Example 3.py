# let us define a class with add method
class operatoroverloading:

    def add(self, a, b):
        self.c = a + b
        return self.c


# creating an object of class
obj = operatoroverloading()

# using add method by passing integers
# as argument
result = obj.add(23, 9)
print("sum is", result)

# using same add method by passing strings
# as argument
result = obj.add("23", "9")
print("Concatenated string is", result)
