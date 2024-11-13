# Import the requests library
import requests

# Test FastAPI using requests library
print(requests.get("http://127.0.0.1:8000/").json())
