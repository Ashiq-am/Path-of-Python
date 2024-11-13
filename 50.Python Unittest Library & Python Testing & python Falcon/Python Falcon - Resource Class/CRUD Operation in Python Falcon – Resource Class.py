import falcon
import json


class TaskResource:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    # Get Method in Falcon
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = {"tasks": self.tasks}

    # Post Method in Falcon
    def on_post(self, req, resp):
        data = json.loads(req.bounded_stream.read().decode("utf-8"))

        if "title" not in data:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Title is required"}
            return

        new_task = {"id": self.next_id, "title": data["title"]}
        self.tasks.append(new_task)
        self.next_id += 1

        resp.status = falcon.HTTP_201
        resp.media = new_task

    # Put Method in Falcon
    def on_put(self, req, resp):
        data = json.loads(req.bounded_stream.read().decode("utf-8"))

        if "current_title" not in data or "new_title" not in data:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Both current_title and new_title are required"}
            return

        for task in self.tasks:
            if task["title"] == data["current_title"]:
                task["title"] = data["new_title"]
                resp.status = falcon.HTTP_200
                resp.media = task
                return

        resp.status = falcon.HTTP_404
        resp.media = {"error": "Task not found"}

    # Delete Method in Falcon
    def on_delete(self, req, resp):
        data = json.loads(req.bounded_stream.read().decode("utf-8"))

        if "title" not in data:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Title is required"}
            return

        for task in self.tasks:
            if task["title"] == data["title"]:
                self.tasks.remove(task)
                resp.status = falcon.HTTP_200
                resp.media = {"message": "Task deleted"}
                return

        resp.status = falcon.HTTP_404
        resp.media = {"error": "Task not found"}


# Create a Falcon app
app = falcon.App()

# Create an instance of TaskResource
task_resource = TaskResource()

# Add routes to the app
app.add_route("/tasks", task_resource)

# HTML UI (cleaned up)
html_ui = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Task Manager</title>
	<style>
		body {
			font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
			background-color: #f9f9f9;
			margin: 0;
			padding: 0;
		}

		header {
			background-color: #333; 
			color: #fff;
			text-align: center;
			padding: 1rem;
		}

		main {
			max-width: 800px;
			margin: 20px auto;
			background-color: #fff;
			padding: 20px;
			border-radius: 8px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
		}

		form {
			display: flex;
			gap: 10px;
			margin-bottom: 20px;
		}

		label {
			font-weight: bold;
			color: #333;
		}

		input {
			padding: 8px;
			border: 1px solid #ccc;
			border-radius: 3px;
			width: 70%;
			font-size: 14px;
		}

		button {
			padding: 8px 15px;
			background-color: #007bff;
			color: #fff;
			border: none;
			border-radius: 3px;
			cursor: pointer;
			font-size: 14px;
		}

		button:hover {
			background-color: #0056b3;
		}

		h1 {
			color: white;
			font-size: 1.5rem;
			margin-bottom: 10px;
		}

		h2 {
			color: #28a745;
			font-size: 3rem;
		}

		ul {
			list-style-type: none;
			padding: 0;
		}

		li {
			margin: 10px 0;
			padding: 10px;
			border: 1px solid #ccc;
			border-radius: 5px;
			display: flex;
			justify-content: space-between;
			align-items: center;
		}

		li:hover {
			background-color: #f0f0f0;
		}

		button.update,
		button.delete {
			padding: 5px 10px;
			font-size: 0.9rem;
		}

		button.update {
			background-color: green;
			color: #fff;
			border: none;
			margin-right: 5px;
		}

		button.delete {
			background-color: red;
			color: #fff;
			border: none;
		}
	</style>
</head>
<body>
	<header>
		<h2>GeeksforGeeks</h2>
		<h1>Task Manager</h1>
	</header>

	<main>
		<form id="taskForm">
			<label for="taskTitle">Task Title:</label>
			<input type="text" id="taskTitle" required>
			<button type="submit">Add Task</button>
		</form>

		<h3>Task List</h3>
		<ul id="taskList"></ul>
	</main>

	<script>
	function fetchTasks() {
		fetch('/tasks')
			.then(response => response.json())
			.then(data => {
				const taskList = document.getElementById('taskList');
				taskList.innerHTML = '';

				data.tasks.forEach(task => {
					const listItem = document.createElement('li');
					listItem.textContent = task.title;

					const updateButton = document.createElement('button');
					updateButton.textContent = 'Update';
					updateButton.onclick = () => handleUpdate(task.title);
					listItem.appendChild(updateButton);

					const deleteButton = document.createElement('button');
					deleteButton.textContent = 'Delete';
					deleteButton.onclick = () => handleDelete(task.title);
					listItem.appendChild(deleteButton);

					taskList.appendChild(listItem);
				});
			});
	}

	function handleFormSubmission(event) {
		event.preventDefault();

		const taskTitle = document.getElementById('taskTitle').value;

		fetch('/tasks', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ title: taskTitle }),
		})
		.then(response => response.json())
		.then(data => {
			console.log('Task added:', data);
			fetchTasks();
		});

		document.getElementById('taskTitle').value = '';
	}

	function handleUpdate(currentTitle) {
		const newTitle = prompt('Enter new title:');
		if (newTitle !== null) {
			fetch('/tasks', {
				method: 'PUT',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({ current_title: currentTitle, new_title: newTitle }),
			})
			.then(response => response.json())
			.then(data => {
				console.log('Task updated:', data);
				fetchTasks();
			});
		}
	}

	function handleDelete(title) {
		const confirmDelete = confirm(`Are you sure you want to delete the task "${title}"?`);
		if (confirmDelete) {
			fetch('/tasks', {
				method: 'DELETE',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({ title: title }),
			})
			.then(response => response.json())
			.then(data => {
				console.log('Task deleted:', data);
				fetchTasks();
			});
		}
	}
	document.getElementById('taskForm').addEventListener('submit', handleFormSubmission);
	fetchTasks();
</script>
</body>
</html>
"""


# Falcon route to serve the HTML UI
class HTMLResource:
    def on_get(self, req, resp):
        resp.content_type = "text/html"
        resp.text = html_ui


app.add_route("/", HTMLResource())

# Run the app
if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    print("Serving on http://127.0.0.1:8000")
    httpd.serve_forever()
