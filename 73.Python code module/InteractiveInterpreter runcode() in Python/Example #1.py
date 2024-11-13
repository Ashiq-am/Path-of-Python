# import code and InteractiveInterpreter
import code
from code import InteractiveInterpreter

source = 'print("GeeksForGeeks")'
compile_code = code.compile_command(source)

# Using InteractiveInterpreter.runcode() method
InteractiveInterpreter().runcode(compile_code)
