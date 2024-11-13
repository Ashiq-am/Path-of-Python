# Pydantic model for response data
class ItemResponse(BaseModel):
	id: int
	name: str
	description: str
