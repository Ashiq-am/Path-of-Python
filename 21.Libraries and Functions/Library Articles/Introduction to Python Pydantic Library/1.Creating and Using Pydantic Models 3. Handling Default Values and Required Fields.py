class UserProfile(BaseModel):
    name: str
    age: int = 43  # Default value
    email: str
    is_active: bool = True  # Default value

user = UserProfile(name="Shrinivas", email="shrinivas3456@gmail.com")
print(user)
