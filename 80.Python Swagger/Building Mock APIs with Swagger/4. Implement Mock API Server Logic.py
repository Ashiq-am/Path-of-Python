from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template_file='swagger.yml')

todos = []

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

api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoResource, '/todos/<int:todo_id>')

if __name__ == '__main__':
	app.run(debug=True)
