from pydantic import BaseModel
import json

class UserProfile(BaseModel):
    name: str
    age: int
    email: str


user = UserProfile(name="Shrinivas", age=22, email="shrinivas3456@gmail.com")

json_data = user.json()
print(json_data)
