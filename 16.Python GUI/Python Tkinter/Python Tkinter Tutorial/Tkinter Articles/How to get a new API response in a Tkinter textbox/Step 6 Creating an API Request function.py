def get_quote():
	r = requests.get('https://api.quotable.io/random')
	data = r.json()
	quote = data['content']
	text_box.delete('1.0', END)
	text_box.insert(END, quote)
