import falcon
from falcon_cors import CORS

# Create a Falcon API instance
app = falcon.App()

# Enable CORS
cors = CORS(allow_all_origins=True, allow_all_headers=True, allow_all_methods=True)
app.add_middleware(cors.middleware)


class FeedbackResource:
	def on_post(self, req, resp):
		# Parse the JSON data from the request body
		feedback_data = req.media

		# Process the feedback (in a real application, you might save it to a database)
		print(f"Received feedback: {feedback_data}")

		# Construct HTML response
		html_response = """
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Feedback Response</title>
			<style>
				body {
					font-family: Arial, sans-serif;
					background-color: #f4f4f4;
					margin: 0;
					padding: 0;
					display: flex;
					justify-content: center;
					align-items: center;
					height: 100vh;
					flex-direction: column;
				}

				h1 {
					color: green;
				}

				#response {
					font-size: 18px;
					color: #333;
					display: flex;
					align-items: center;
				}

				.tick {
					margin-right: 10px;
					color: #4caf50;
				}
			</style>
		</head>
		<body>
			<h1>GeeksforGeeks</h1>
			<div id="response">
				<span class="tick"></span> Feedback received successfully
			</div>
		</body>
		</html>
		"""

		# Set the HTML response
		resp.content_type = falcon.MEDIA_HTML
		resp.text = html_response
		resp.status = falcon.HTTP_200


# Add the FeedbackResource to the API
app.add_route("/feedback", FeedbackResource())

if __name__ == "__main__":
	from wsgiref import simple_server

	# Run the Falcon API
	httpd = simple_server.make_server("127.0.0.1", 8000, app)
	print("Serving on http://127.0.0.1:8000")
	httpd.serve_forever()
