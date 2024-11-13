import uvicorn
import falcon
import falcon.asgi
import jinja2

html = """
<!DOCTYPE html>
<html>
   <head>
      <title>GeeksforGeeks Chat</title>
      <style>
         body {
            background-color: #f0f8ea;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
         }
         #chat-container {
            width: 400px;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
         }
      </style>
   </head>
   <body>
      <div id="chat-container">
         <h1>GeeksforGeeks Chat</h1>
         <ul id='messages'></ul>
         <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
         </form>
      </div>
      <script>
         var ws = new WebSocket("ws://localhost:8000/chat");
         ws.onmessage = function(event) {
            var messages = document.getElementById('messages');
            var message = document.createElement('li');
            var content = document.createTextNode(event.data);
            message.appendChild(content);
            messages.appendChild(message);
         };
         function sendMessage(event) {
            var input = document.getElementById("messageText");
            ws.send(input.value);
            input.value = '';
            event.preventDefault();
         }
      </script>
   </body>
</html>
"""


class ChatResource:
    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        template = jinja2.Template(html)
        resp.body = template.render()

    async def on_websocket(self, req, websocket):
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message: {data}")


app = falcon.asgi.App()
chat = ChatResource()
app.add_route('/chat', chat)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
