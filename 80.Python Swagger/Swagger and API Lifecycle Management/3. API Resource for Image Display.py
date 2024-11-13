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
