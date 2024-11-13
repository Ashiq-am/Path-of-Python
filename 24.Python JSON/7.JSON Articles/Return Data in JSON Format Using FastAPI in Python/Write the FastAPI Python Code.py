from fastapi import FastAPI

app = FastAPI()

@app.get("/Hello-world")
def Hello():
	data = {
		"message": "hello world",
		"details": {
			"author": {
				"name": "Tushar",
				"email": "tushar@example.com"
			},
			"tags": ["fastapi", "python", "web"]

		}
	}
	return data
