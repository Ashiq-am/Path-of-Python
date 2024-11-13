from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def Hello_World(request):
	return Response('Hello World')


if __name__ == '__main__':
	with Configurator() as Config:
		Config.add_route('helloworld', '/')
		Config.add_view(Hello_World, route_name='helloworld')
		app = Config.make_wsgi_app()
	server = make_server('0.0.0.0', 5000, app)
	server.serve_forever()
