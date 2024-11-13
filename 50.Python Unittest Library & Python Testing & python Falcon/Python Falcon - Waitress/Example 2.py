# Import the necessary modules
from waitress import serve
import falcon


# Define a Falcon resource class
class UserResource:
	def on_get(self, req, resp, username):
		resp.status = falcon.HTTP_200
		resp.content_type = falcon.MEDIA_TEXT
		resp.text = f"Hello, {username} !"


# Create a Falcon application
app = falcon.App()

# Create an instance of the UserResource class
userResource = UserResource()

# Add a route to the Falcon app, mapping the root URL
# ('/user/{username}') to the MyResource instance
# `username` is dynamic field, which we get from URL
app.add_route("/user/{username}", userResource)

# Check if the script is executed as the main program
if __name__ == "__main__":
	# Print a message to indicate the server is starting
	print("Server is starting on http://127.0.0.1:8000")

	# Serve the Falcon app using Waitress, specifying
	# the host and port
	serve(app, host="127.0.0.1", port=8000)
