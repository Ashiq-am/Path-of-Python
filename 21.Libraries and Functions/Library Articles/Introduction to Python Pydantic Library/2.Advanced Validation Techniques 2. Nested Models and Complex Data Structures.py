class Address(BaseModel):
    street: str
    city: str

class UserProfile(BaseModel):
    name: str
    age: int
    email: str
    address: Address

address = Address(street="461 soraon kauri", city="Prayagraj")
user = UserProfile(name="Rekha", age= 40, email="rekhashri7342@gmail.com", address=address)
print(user)
