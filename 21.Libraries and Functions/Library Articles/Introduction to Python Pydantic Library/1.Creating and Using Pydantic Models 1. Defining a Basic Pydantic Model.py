from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

user = UserProfile(name="Rekha ", age=40, email="rekhashri345@gmail.com")
print(user)
