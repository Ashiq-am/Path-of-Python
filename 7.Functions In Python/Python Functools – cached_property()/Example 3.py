# Without using @cached_property

# A sample class
class Sample():

    def __init__(self, lst):
        self.long_list = lst

    # a method to find the sum of the
    # given long list of integer values
    def find_sum(self):
        return (sum(self.long_list))

# obj is an instance of the class sample
# the list can be longer, this is just
# an example
obj = Sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(obj.find_sum())
print(obj.find_sum())
print(obj.find_sum())
