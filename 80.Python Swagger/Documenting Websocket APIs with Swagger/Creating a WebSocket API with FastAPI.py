from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Test</title>
</head>
<body>
    <h1>WebSocket Test</h1>
    <form id="form">
        <input type="text" id="messageInput" autocomplete="off"/>
        <button>Send</button>
    </form>
    <ul id="messages"></ul>
    <script>
        const form = document.getElementById('form');
        const input = document.getElementById('messageInput');
        const messages = document.getElementById('messages');

        const ws = new WebSocket('ws://localhost:8000/ws');

        ws.onmessage = function(event) {
            const li = document.createElement('li');
            li.textContent = event.data;
            messages.appendChild(li);
        };

        form.addEventListener('submit', function(event) {
            event.preventDefault();
            ws.send(input.value);
            input.value = '';
        });
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
