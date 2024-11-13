api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoResource, '/todos/<int:todo_id>')

if __name__ == '__main__':
	app.run(debug=True)
