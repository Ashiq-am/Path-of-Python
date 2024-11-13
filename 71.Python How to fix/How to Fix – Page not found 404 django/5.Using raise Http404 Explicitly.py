from django.http import Http404

def my_view(request):
	if some_condition:
		raise Http404("This page does not exist.")
	# ...
