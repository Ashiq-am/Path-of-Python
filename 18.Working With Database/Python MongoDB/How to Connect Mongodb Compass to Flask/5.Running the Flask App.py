@app.route('/') 
# ‘/’ URL is bound with hello_world() function. 
def hello_world(): 
	documents = collection.find() 
	for record in documents: 
		print(record) 
	return "HEllo"
# main driver function 
if __name__ == '__main__': 

	# run() method of Flask class runs the application 
	# on the local development server. 
	app.run()
