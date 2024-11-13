import falcon
from resources import HelloResource

app = falcon.App()
hello = HelloResource()

app.add_route('/hello', hello)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='127.0.0.1', port=8000)
