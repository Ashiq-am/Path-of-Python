from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/Hello-world")
def hello():
	data = {
		"message": "Hello, world!",
		"details": {
			"author": {
				"name": "Tushar",
				"email": "tushar@example.com"
			},
			"tags": ["fastapi", "python", "web"]
		}
	}

	return data
