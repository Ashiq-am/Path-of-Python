@app.route('/<user_handle>/')
def home(user_handle):

	response = get_profile_detail(user_handle)
	if response:
		response.update(get_articles_and_improvements(user_handle))
		api_response = make_response(jsonify(response), 200)
	else:
		response = {'message': 'No such user with the specified handle'}
		api_response = make_response(jsonify(response), 404)
	api_response.headers['Content-Type'] = 'application/json'
	return api_response
