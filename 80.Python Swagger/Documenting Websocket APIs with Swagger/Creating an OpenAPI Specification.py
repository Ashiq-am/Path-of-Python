from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="WebSocket API",
        version="1.0.0",
        description="This is a simple WebSocket API",
        routes=app.routes,
    )
    openapi_schema["paths"]["/ws"] = {
        "get": {
            "summary": "WebSocket connection",
            "description": "Connect to the WebSocket server. Send a message and receive a response.",
            "responses": {
                "101": {
                    "description": "Switching Protocols - The client is switching protocols as requested by the server.",
                }
            }
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
