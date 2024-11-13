from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home',
			renderer='templates/postindex.jinja2')
def home(request):
	return {}


@view_config(route_name='register',
			request_method='POST',
			renderer='templates/poststudentregistration.jinja2')
def register(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	password = request.POST.get('password')
	return {}


@view_config(route_name='successful')
def successful(request):
	return Response("Successfully Submitted")


if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	config = Configurator()
	config.include('pyramid_jinja2')
	config.add_route('home', '/')
	config.add_route('register', '/register')
	config.add_route('successful', '/successful')
	config.scan()
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 8080, app)
	server.serve_forever()
