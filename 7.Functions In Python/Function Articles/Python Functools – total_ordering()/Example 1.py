from functools import total_ordering


@total_ordering
class Students:
    def __init__(self, cgpa):
        self.cgpa = cgpa

    def __lt__(self, other):
        return self.cgpa < other.cgpa

    def __eq__(self, other):
        return self.cgpa == other.cgpa

    def __le__(self, other):
        return self.cgpa <= other.cgpa

    def __ge__(self, other):
        return self.cgpa >= other.cgpa

    def __ne__(self, other):
        return self.cgpa != other.cgpa


Arjun = Students(8.6)

Ram = Students(7.5)

print(Arjun.__lt__(Ram))
print(Arjun.__le__(Ram))
print(Arjun.__gt__(Ram))
print(Arjun.__ge__(Ram))
print(Arjun.__eq__(Ram))
print(Arjun.__ne__(Ram))
