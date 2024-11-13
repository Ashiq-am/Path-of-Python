@app.route('/add_data', methods=['POST'])
def add_data():
	# Get data from request
	data = request.json

	# Insert data into MongoDB
	collection.insert_one(data)

	return 'Data added to MongoDB'
