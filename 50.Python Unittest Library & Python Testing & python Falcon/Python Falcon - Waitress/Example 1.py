# Import the necessary modules
from waitress import serve
import falcon


# Define a Falcon resource class
class MyResource:
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
		resp.content_type = falcon.MEDIA_TEXT
		resp.text = "Hello, GFG User !"


# Create a Falcon application
app = falcon.App()

# Create an instance of the MyResource class
myResource = MyResource()

# Add a route to the Falcon app, mapping the root URL ('/') to the MyResource instance
app.add_route("/", myResource)

# Check if the script is executed as the main program
if __name__ == "__main__":
	# Print a message to indicate the server is starting
	print("Server is starting on http://127.0.0.1:8000")

	# Serve the Falcon app using Waitress, specifying the host and port
	serve(app, host="127.0.0.1", port=8000)
