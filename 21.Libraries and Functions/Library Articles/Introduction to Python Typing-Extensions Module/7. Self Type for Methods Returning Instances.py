from typing_extensions import Self

class Builder:
    def set_name(self, name: str) -> Self:
        self.name = name
        return self

    def build(self) -> dict:
        return {'name': self.name}

builder = Builder().set_name('Example').build()
print(builder)
