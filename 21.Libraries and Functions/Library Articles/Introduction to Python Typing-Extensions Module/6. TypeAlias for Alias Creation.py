from typing_extensions import TypeAlias

# Alias for a tuple of two integers
Coordinate: TypeAlias = tuple[int, int]

def move_to(position: Coordinate) -> None:
    print(f"Moving to {position}")

move_to((10, 20))
