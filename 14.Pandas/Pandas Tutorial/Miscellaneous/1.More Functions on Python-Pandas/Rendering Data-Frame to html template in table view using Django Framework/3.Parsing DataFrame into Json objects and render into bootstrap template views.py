# Write Python3 code here
from django.shortcuts import render
import pandas as pd
import json

# Create your views here.
def Table(request):
	df = pd.read_csv("tableview/static/csv/20_Startups.csv")

	# parsing the DataFrame in json format.
	json_records = df.reset_index().to_json(orient ='records')
	data = []
	data = json.loads(json_records)
	context = {'d': data}

	return render(request, 'table.html', context)
