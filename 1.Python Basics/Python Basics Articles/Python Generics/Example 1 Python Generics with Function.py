from typing import TypeVar, List

T = TypeVar('T')

def element(items: List[T]) -> T:
    return items[0]

# Usage
print(element([1, 2, 3]))
print(element(['a', 'b', 'c']))
