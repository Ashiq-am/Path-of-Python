import falcon

class QueryParamsResource:
	def on_get(self, req, resp):
		# Retrieve query parameters
		name = req.get_param('name', default=None)
		age = req.get_param_as_int('age', default=None)

		# Process parameters and generate response
		response = {'message': 'Query parameters received successfully'}

		if name:
			response['name'] = name

		if age is not None:
			response['age'] = age

		resp.status = falcon.HTTP_200
		resp.media = response

app.add_route('/query', QueryParamsResource())
