# Pydantic model for request data
class ItemCreate(BaseModel):
	name: str
	description: str
