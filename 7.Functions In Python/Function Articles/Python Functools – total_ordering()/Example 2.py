from functools import total_ordering


@total_ordering
class num:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        # Changing the functionality
        # of equality operator
        return self.value != other.value


# Driver code
print(num(2) < num(3))
print(num(2) > num(3))
print(num(3) == num(3))
print(num(3) == num(5))
