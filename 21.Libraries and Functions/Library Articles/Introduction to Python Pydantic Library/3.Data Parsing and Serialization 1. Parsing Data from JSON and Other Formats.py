from pydantic import BaseModel
import json

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

data = '{"name": "Rekha", "age": 40, "email": "rekhashri7354@gmail.com"}'
user = UserProfile.parse_raw(data)
print(user)
