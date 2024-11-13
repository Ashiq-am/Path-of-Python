import json

swagger_definition = {
	"swagger": "2.0",
	"info": {
		"title": "My API",
		"version": "1.0.0",
	},
	"paths": {
		"/detailed-endpoint": {
			"get": {
				"summary": "Detailed Endpoint",
				"x-description": """
					This endpoint provides detailed information.
					You can use it for various purposes.
				""",
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
