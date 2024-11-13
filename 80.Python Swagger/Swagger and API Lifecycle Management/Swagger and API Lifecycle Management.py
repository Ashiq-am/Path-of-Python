from flask import Flask, request, send_file
from flask_restx import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
from PIL import Image
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='Image Upload API',
          description='API for uploading and displaying images')

upload_parser = api.parser()
upload_parser.add_argument('image', location='files',
                           type=FileStorage, required=True,
                           help='Image file')

image_store = "uploaded_images"

if not os.path.exists(image_store):
    os.makedirs(image_store)


@api.route('/upload')
class ImageUpload(Resource):
    @api.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        image_file = args['image']

        image_path = os.path.join(image_store,
                                  image_file.filename)
        image_file.save(image_path)

        # Resize image if needed
        resized_path = os.path.join(image_store,
                                    "resized_" + image_file.filename)
        with Image.open(image_path) as img:
            img.thumbnail((300, 300))
            img.save(resized_path)

        return {'message': 'Image uploaded successfully',
                'image_path': resized_path}


@api.route('/image/<string:image_name>')
class ImageDisplay(Resource):
    def get(self, image_name):
        image_path = os.path.join(image_store, image_name)
        if os.path.exists(image_path):
            return send_file(image_path, mimetype='image/jpeg')
        else:
            return {'message': 'Image not found'}, 404


if __name__ == '__main__':
    app.run(debug=True)
