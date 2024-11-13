import json

swagger_definition = {
	"swagger": "2.0",
	"info": {
		"title": "My API",
		"version": "1.0.0",
	},
	"x-logo": "https://example.com/logo.png",
	"paths": {
		"/endpoint": {
			"get": {
				"summary": "Get Data",
				"description": "Retrieves data from the API.",
				"responses": {
					"200": {
						"description": "Successful response."
					}
				}
			}
		}
	}
}

with open('swagger.json', 'w') as f:
	json.dump(swagger_definition, f)
