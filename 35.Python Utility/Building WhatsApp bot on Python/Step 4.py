# chatbot logic
def bot():

	# user input
	user_msg = request.values.get('Body', '').lower()

	# creating object of MessagingResponse
	response = MessagingResponse()

	# User Query
	q = user_msg + "geeksforgeeks.org"

	# list to store urls
	result = []

	# searching and storing urls
	for i in search(q, tld='co.in', num=6, stop=6, pause=2):
		result.append(i)

	# displaying result
	msg = response.message(f"--- Result for '{user_msg}' are ---")

	msg = response.message(result[0])
	msg = response.message(result[1])
	msg = response.message(result[2])
	msg = response.message(result[3])
	msg = response.message(result[4])

	return str(response)
