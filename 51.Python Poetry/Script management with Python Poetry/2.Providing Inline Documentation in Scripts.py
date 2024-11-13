# my_project/scripts.py

def say_hello():
    """
    Prints 'Hello, world!' to the console.
    """
    print("Hello, world!")

def run_server():
    """
    Starts a simple HTTP server on port 8000.

    This server serves files from the current directory.
    """
    import http.server
    import socketserver

    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
