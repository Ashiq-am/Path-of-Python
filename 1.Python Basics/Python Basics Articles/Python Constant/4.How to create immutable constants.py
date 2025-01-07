from collections import namedtuple

Constants = namedtuple('Constants', ['PI', 'GRAVITY'])
constants = Constants(PI=3.14159, GRAVITY=9.8)

# constants.PI = 3.14
print(constants.PI)