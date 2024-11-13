class RectangleClass(object):
    def __init__(self, area, breadth):
        self._area = area
        self._breadth = breadth

    def __len__(self):
        return int(self._area / self._breadth)


rc = RectangleClass(90, 5)
print(len(rc))
