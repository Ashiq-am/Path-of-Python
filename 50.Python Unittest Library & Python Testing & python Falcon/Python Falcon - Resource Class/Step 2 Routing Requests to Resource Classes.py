import falcon
app = falcon.App()
hello_world_resource = HelloWorldResource()
app.add_route('/hello', hello_world_resource)
