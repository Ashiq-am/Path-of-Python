class RectangleClass(object):
    def __init__(self, area, breadth):
        self._area = area
        self._breadth = breadth

    def __len__(self):
        return int(self._area / self._breadth)

    def __repr__(self):
        """object representation"""
        return 'RectangleClass(area =% d, breadth =% d)' % \
               (self._area, self._breadth)


RectangleClass(90, 5)
RectangleClass(80, 4)
