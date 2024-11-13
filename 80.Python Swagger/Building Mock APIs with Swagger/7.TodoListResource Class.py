class TodoListResource(Resource):
	def get(self):
		return {'todos': todos}

	def post(self):
		new_todo = {
			'id': len(todos) + 1,
			'task': request.json['task'],
			'completed': request.json.get('completed', False)
		}
		todos.append(new_todo)
		return {'message': 'Todo created successfully'}, 201
