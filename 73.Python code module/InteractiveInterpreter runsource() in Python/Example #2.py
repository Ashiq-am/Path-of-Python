# import code and InteractiveInterpreter
from code import InteractiveInterpreter

code = 'a = 8; b = 2.5; -a = a + b'
# Using InteractiveInterpreter.runsource() method
InteractiveInterpreter().runsource(code)
