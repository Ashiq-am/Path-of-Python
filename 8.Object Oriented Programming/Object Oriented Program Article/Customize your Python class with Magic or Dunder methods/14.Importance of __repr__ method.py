class RectangleClass(object):
    def __init__(self, area, breadth):
        self._area = area
        self._breadth = breadth

    def __len__(self):
        return int(self._area / self._breadth)


## use python interactive terminal to check object representation.
RectangleClass(90, 5)
