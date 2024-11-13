from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from

app = Flask(__name__)
api = Api(app)

# Configuring Swagger
app.config['SWAGGER'] = {
    'title': 'My API',
    'uiversion': 3
}
swagger = Swagger(app)

class Welcome(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'A status code 200 means successful and returns a message.',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Successful response',
                                'value': {'message': 'Welcome GeeksforGeeks!!'}
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self):
        """
        This is an example endpoint which returns a simple message.
        """
        return {'message': 'Welcome GeeksforGeeks!!'}


api.add_resource(Welcome, '/')


if __name__ == '__main__':
    app.run(debug=True)
