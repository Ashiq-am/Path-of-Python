from pydantic import BaseModel, field_validator

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

    @field_validator('age')
    def check_age(cls, value):
        if value < 40:
            raise ValueError('Age must be at least 18')
        return value

UserProfile(name="Rekha", age=17, email="rekha@gmail.com")
