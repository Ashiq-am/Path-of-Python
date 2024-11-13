# code
from collections.abc import Iterable

name = 'Roster'

if isinstance(name, Iterable):
    print(f"{name} is iterable")

else:
    print(f"{name} is not iterable")
