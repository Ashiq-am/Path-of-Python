class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x

l = [Point(1, 15), Point(10, 5), Point(3, 8)]
l.sort()

for i in l:
    print(i.x, i.y)
