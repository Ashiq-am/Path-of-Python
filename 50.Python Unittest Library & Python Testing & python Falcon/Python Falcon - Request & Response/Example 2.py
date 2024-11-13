import falcon

# GeeksforGeeks Courses Data in JSON format
course_data = [
	{
		"name": "DSA to Development: A Complete Guide",
		"level": "Beginner to Advance",
		"interest": "125k+ interested Geeks",
		"rating": "5",
	},
	{
		"name": "Full Stack Development with React & Node JS - Live",
		"level": "Beginner to Advance",
		"interest": "195k+ interested Geeks",
		"rating": "4.7",
	},
]


# Define a Falcon resource class named CourseCartResource
class CourseCartResource:
	def on_get(self, req, resp):
		# Convert the list of courses to an HTML response
		html_data = (
			"<html>\n<head><title>GeeksforGeeks Course Cart</title></head>\n<body>\n"
		)
		html_data += "<h1>GeeksforGeeks Course Cart</h1>\n<ul>\n"
		for course in course_data:
			html_data += (
				f"<li><strong>{course['name']}</strong><br>"
				f"Level: {course['level']}<br>"
				f"Interest: {course['interest']}<br>"
				f"Rating: {course['rating']}</li>\n"
			)
		html_data += "</ul>\n</body>\n</html>"

		# Set response attributes for HTML format
		resp.status = falcon.HTTP_200
		resp.text = html_data
		resp.content_type = "text/html"
		resp.set_header("Cache-Control", "no-cache")


# Create a Falcon App instance
app = falcon.App()

# Add the CourseCartResource to the App, associating it with the '/course-cart' endpoint
app.add_route("/course-cart", CourseCartResource())

if __name__ == "__main__":
	from wsgiref import simple_server

	# Set the host and port for the Falcon application
	host = "127.0.0.1"
	port = 8000

	# Create a simple WSGI server using wsgiref and serve the Falcon application
	httpd = simple_server.make_server(host, port, app)
	print(f"Serving on http://{host}:{port}")
	# Serve requests indefinitely
	httpd.serve_forever()
