import json

swagger_definition = {
	"swagger": "2.0",
	"info": {
		"title": "My API",
		"version": "1.0.0",
	},
	"paths": {
		"/secure-endpoint": {
			"get": {
				"summary": "Secure Endpoint",
				"responses": {
					"200": {
						"description": "Successful response."
					}
				},
				"security": [{
					"api_key": []
				}]
			}
		}
	},
	"securityDefinitions": {
		"api_key": {
			"type": "apiKey",
			"in": "header",
			"name": "x-auth-token"
		}
	}
}


with open('swagger.json', 'w') as f:
	json.dump(swagger_definition, f)
