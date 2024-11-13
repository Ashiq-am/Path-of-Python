# import sympy
from typing import List

from sympy import *

# Use sympy.fromiter() method
gfg = List.fromiter(i for i in range(10))

print(gfg)
