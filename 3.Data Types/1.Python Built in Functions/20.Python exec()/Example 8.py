#__builtins__ has been restricted using None
from math import *
exec("print(dir())", {"__builtins__" : None}, {"sum": sum, "print": print, "dir": dir})
