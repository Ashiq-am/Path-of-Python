# API endpoint to create an item
@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
	db_item = Item(**item.model_dump())
	db.add(db_item)
	db.commit()
	db.refresh(db_item)
	return db_item
