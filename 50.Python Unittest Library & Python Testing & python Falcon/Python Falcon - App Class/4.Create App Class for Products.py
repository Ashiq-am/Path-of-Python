import falcon

class ProductResource:
    def on_get(self, req, resp):
        # Logic to fetch and return product catalog data from database
        resp.media = {'products': [{'id': 1, 'name': 'Product A', 'price': 20.99},
                                   {'id': 2, 'name': 'Product B', 'price': 15.49}]}

class ProductDetailResource:
    def on_get(self, req, resp, product_id):
        # Logic to fetch and return product details based on product_id
        resp.media = {'product_id': product_id, 'name': 'Product A', 'price': 20.99, 'description': 'Lorem ipsum'}

app = falcon.App()
app.add_route('/products', ProductResource())
app.add_route('/products/{product_id}', ProductDetailResource())

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, app)
    print('Serving on localhost:8000...')
    httpd.serve_forever()
