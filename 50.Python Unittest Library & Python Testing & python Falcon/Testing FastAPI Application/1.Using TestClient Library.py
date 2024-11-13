# Import the FastAPI and TestClient libraries
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Create a FastAPI application
app = FastAPI()

# Call FastAPI using Pydantic
@app.get("/")
async def read_main():
	return {"msg": "Welcome to Geeks For Geeks"}

# Create a Test Client for FastAPI app
client = TestClient(app)

# Test FastAPI using TestClient
def test_read_main():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"msg": "Welcome to Geeks For Geeks"}
