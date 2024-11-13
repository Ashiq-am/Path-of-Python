import falcon
from resources import UserResource

# Create the Falcon application
app = falcon.App()

# Instantiate the user resource
user_resource = UserResource()

# Add routes
app.add_route('/users/{user_id:int}', user_resource)
app.add_route('/users', user_resource)
