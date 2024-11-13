from typing import Optional
from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: Optional[int] = None
    email: str
