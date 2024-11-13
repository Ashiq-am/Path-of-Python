from django.shortcuts import get_object_or_404
from .models import YourModel

def detail_view(request, object_id):
	obj = get_object_or_404(YourModel, pk=object_id)
	# ...
