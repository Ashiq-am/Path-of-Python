@app.callback(
	Output(component_id ='output', component_property ='children'),
	[Input(component_id ='input', component_property ='value')]
)

def update_value(input_data):
	try:
		return str(float(input_data)**2)
	except:
		return "Error, the input is not a number"
