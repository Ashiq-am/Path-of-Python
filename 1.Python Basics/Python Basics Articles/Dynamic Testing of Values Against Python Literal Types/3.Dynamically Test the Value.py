from typing import get_args, get_origin, Literal

def check_literal_type(value, literal_type):
    if get_origin(literal_type) is Literal:
        return value in get_args(literal_type)
    raise TypeError(f"{literal_type} is not a Literal type")

# Example usage
print(check_literal_type(2, MyLiteralInt))       # True
print(check_literal_type("apple", MyLiteralStr)) # True
print(check_literal_type(False, MyLiteralBool))  # True
print(check_literal_type(4, MyLiteralInt))       # False
print(check_literal_type("banana", MyLiteralStr))# True
print(check_literal_type(True, MyLiteralBool))   # True
print(check_literal_type("grape", MyLiteralStr)) # False
