# API endpoint to read an item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
	db_item = db.query(Item).filter(Item.id == item_id).first()
	if db_item is None:
		raise HTTPException(status_code=404, detail="Item not found")
	return db_item
