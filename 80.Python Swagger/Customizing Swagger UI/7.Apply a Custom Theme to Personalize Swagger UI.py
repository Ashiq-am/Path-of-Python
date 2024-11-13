from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="Custom API",
    description="This is a custom description for the API.",
    version="1.0.0"
)

@app.get("/items/{item_id}", tags=["items"])
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/docs", include_in_schema=True)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_ui_html="custom_swagger_ui.html"
    )

@app.get("/openapi.json", include_in_schema=True)
async def openapi():
    return get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
