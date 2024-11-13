from typing import TypeVar, Generic

T = TypeVar(Generic[T])


class Container:
    def __init__(self, content: T):
        self.content = content

    def retrieve_content(self) -> T:
        return self.content


# Usage
container_int = Container(10)
container_str = Container('GeeksforGeeks')

print(container_int.retrieve_content())
print(container_str.retrieve_content())
