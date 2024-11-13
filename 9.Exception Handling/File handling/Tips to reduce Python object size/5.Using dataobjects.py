import sys
from recordclass import make_dataclass

Position = make_dataclass('Position', ('x', 'y', 'z'))
Coordinates = Position(3, 0, 1)

print(sys.getsizeof(Coordinates))
