import falcon
import json

class TaskResource:
	def on_post(self, req, resp):
		try:
			# Retrieve and parse JSON data from the request body
			task_data = json.loads(req.bounded_stream.read().decode('utf-8'))

			# Extract task details
			task_id = task_data.get('task_id')
			title = task_data.get('title')
			completed = task_data.get('completed', False) # Default to False if not provided

			if task_id is not None and title is not None:
				# Process the task (in this example, just printing)
				print(f"New Task - ID: {task_id}, Title: {title}, Completed: {completed}")

				# Build response with task details
				response_data = {
					'message': 'Task created successfully',
					'task_details': {
						'task_id': task_id,
						'title': title,
						'completed': completed
					}
				}

				resp.status = falcon.HTTP_201 # Created
				resp.text = json.dumps(response_data)
			else:
				# Raise an error if task_id or title is missing
				raise ValueError("Both task_id and title are required in the request JSON.")

		except json.JSONDecodeError as e:
			# Handle JSON decoding errors
			resp.status = falcon.HTTP_400 # Bad Request
			resp.text = json.dumps({'error': 'Invalid JSON format'})
		except ValueError as e:
			# Handle missing task_id or title
			resp.status = falcon.HTTP_400 # Bad Request
			resp.text = json.dumps({'error': str(e)})
		except Exception as e:
			# Handle other exceptions
			resp.status = falcon.HTTP_500 # Internal Server Error
			resp.text = json.dumps({'error': 'Internal Server Error'})

# Falcon application
app = falcon.App()
app.add_route('/tasks', TaskResource())

# Run Falcon's development server
if __name__ == '__main__':
	from wsgiref import simple_server

	host = '127.0.0.1'
	port = 8000

	httpd = simple_server.make_server(host, port, app)
	print(f"Serving on http://{host}:{port}")
	httpd.serve_forever()
