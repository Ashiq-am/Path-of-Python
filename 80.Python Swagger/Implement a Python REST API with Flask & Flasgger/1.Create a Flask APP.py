from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    def get(self):
        return {'message': 'Welcome to GeeksforGeeks!'}


api.add_resource(Welcome, '/')

if __name__ == '__main__':
    app.run(debug=True)
