from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import json


@view_config(route_name='home',
			renderer='templates/jsondatarendering.jinja2')
def home(request):
	data = {
		'name': 'Vikash Mishra',
		'field': 'Computer Science',
		'graduation': 'btech',
		'college': 'ITM University Gwalior',
		'skills': ['C', 'C++', 'Python', 'Javascript']

	}
	return {'data': data}


if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	config = Configurator()
	config.include('pyramid_jinja2')
	config.add_route('home', '/')
	config.scan()
	app = config.make_wsgi_app()
	server = make_server('localhost', 8000, app)
	server.serve_forever()
