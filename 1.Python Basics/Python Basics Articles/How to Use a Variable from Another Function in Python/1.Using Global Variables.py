def set_variable():
    global my_variable
    my_variable = "Hello from GeeksforGeeks"

def use_variable():
    global my_variable
    print(my_variable)

set_variable()
use_variable()
