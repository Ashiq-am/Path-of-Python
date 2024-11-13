# falconUvicorn.py
# Importing the necessary modules
import falcon
import falcon.asgi
import uvicorn

# Defining a Falcon resource for handling GET requests

class HelloWorldResource:
	async def on_get(self, req, resp):
		# Setting the HTTP response status to 200 (OK)
		resp.status = falcon.HTTP_200
		# Setting the response content to "Hello, Welcom to GFG portal !"
		resp.text = 'Hello, Welcom to GFG portal !'


# Creating an asynchronous Falcon application instance
app = falcon.asgi.App()

# Creating an instance of the HelloWorldResource
helloResource = HelloWorldResource()

# Adding the HelloWorldResource to the Falcon application with the /hello route
app.add_route('/hello', helloResource)

if __name__ == '__main__':
	# Running the Falcon application with Uvicorn server
	uvicorn.run("falconUvicorn:app", host='127.0.0.1', port=8000, reload=True)
