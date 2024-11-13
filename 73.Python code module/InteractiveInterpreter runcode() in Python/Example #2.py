import code
from code import InteractiveInterpreter

source = 'a = 5; b = 5; li = [a * b for i in range(5)]; print(li)'
compile_code = code.compile_command(source)

# Using InteractiveInterpreter.runcode() method
InteractiveInterpreter().runcode(compile_code)
