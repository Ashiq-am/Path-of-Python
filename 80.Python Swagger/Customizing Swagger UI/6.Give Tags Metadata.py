from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Custom API",
    description="This is a custom description for the API.",
    version="1.0.0"
)

router = APIRouter()


@router.get("/items/{item_id}", tags=["items"])
async def read_item(item_id: int, q: str = None):
    """
    Read an item with a specific ID.

    - **item_id**: The ID of the item you want to retrieve.
    - **q**: An optional query parameter.
    """
    return {"item_id": item_id, "q": q}


app.include_router(router)
