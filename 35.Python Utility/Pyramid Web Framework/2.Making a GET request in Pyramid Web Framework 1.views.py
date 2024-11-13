from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home',
			renderer='templates/getindex.jinja2')
def home(request):
	return {}


@view_config(route_name='studentregistration',
			request_method='GET',
			renderer='templates/getstudentregistration.jinja2')
def register(request):
	name = request.GET.get('name')
	email = request.GET.get('email')
	password = request.GET.get('password')
	return {}


@view_config(route_name='successful')
def successful(request):
	return Response("Successfully Submitted")


if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	config = Configurator()
	config.include('pyramid_jinja2')
	config.add_route('home', '/')
	config.add_route('studentregistration', '/register')
	config.add_route('successful', '/successful')
	config.scan()
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 8080, app)
	server.serve_forever()
