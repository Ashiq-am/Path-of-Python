# import library
import attr


# initialising class Coordinates, no need to
# initialize __init__ method
@attr.s
class Coordinates(object):
    # attributes
    x = attr.ib()
    y = attr.ib()


c1 = Coordinates(1, 2)

# converting data into dict using attr.asdict()
# function
print(attr.asdict(Coordinates(x=1, y=2)))
