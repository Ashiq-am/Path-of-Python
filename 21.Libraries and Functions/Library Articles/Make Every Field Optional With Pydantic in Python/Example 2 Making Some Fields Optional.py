from typing import Optional
from pydantic import BaseModel

class MyModel(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    # Add more fields as needed

# Example 2: Some fields missing
data2 = {"name": "Sushma"}
model2 = MyModel(**data2)
print(model2.dict())
