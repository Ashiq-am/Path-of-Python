# code
from typing import Literal, get_args
Fruit = Literal['apple', 'banana', 'cherry']
def is_fruit(value) -> bool:
    return value in get_args(Fruit)

print(is_fruit('apple'))
print(is_fruit('orange'))
