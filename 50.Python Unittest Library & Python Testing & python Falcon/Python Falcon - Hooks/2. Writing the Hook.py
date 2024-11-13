#app.py
import falcon

# Define the authentication hook
def auth_hook(req, resp, resource, params):
    token = req.get_header('Authorization')
    if token != 'secret-token':
        raise falcon.HTTPUnauthorized('Authentication required',
                                      'Please provide a valid token.')
