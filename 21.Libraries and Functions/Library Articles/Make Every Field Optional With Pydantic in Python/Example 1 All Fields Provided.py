from typing import Optional
from pydantic import BaseModel


class MyModel(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    # Add more fields as needed


# Example Usage
data1 = {"name": "Sushma", "age": 21}
model1 = MyModel(**data1)
print(model1.dict())
