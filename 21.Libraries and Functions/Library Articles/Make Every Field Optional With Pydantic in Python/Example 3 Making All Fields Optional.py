from typing import Optional
from pydantic import BaseModel


class MyModel(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    # Add more fields as needed


# Example 3: All fields missing
data3 = {}
model3 = MyModel(**data3)
print(model3.dict())
