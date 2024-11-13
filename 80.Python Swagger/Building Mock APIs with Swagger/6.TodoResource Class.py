class TodoResource(Resource):
	def get(self, todo_id):
		todo = next((t for t in todos if t['id'] == todo_id), None)
		if todo:
			return todo
		else:
			return {'message': 'Todo not found'}, 404

	def put(self, todo_id):
		todo = next((t for t in todos if t['id'] == todo_id), None)
		if todo:
			todo['task'] = request.json.get('task', todo['task'])
			todo['completed'] = request.json.get(
				'completed', todo['completed'])
			return {'message': 'Todo updated successfully'}
		else:
			return {'message': 'Todo not found'}, 404

	def delete(self, todo_id):
		global todos
		todos = [t for t in todos if t['id'] != todo_id]
		return {'message': 'Todo deleted successfully'}
