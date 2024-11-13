""""""



'''
# .kv file implementation of the .py file 

# Creating the Layout i.e root of the Layout class 
<SampBoxLayout>: 

	# creating the spinner 
	Spinner: 
		# Assigning id 
		id: spinner_id 

		# Callback 
		on_text: root.spinner_clicked(spinner_id.text) 

		# initially text on spinner 
		text: "Python"

		# total values on spinner 
		values: ["Python", "Java", "C++", "C", "C#", "PHP"] 

		# declaring size of the spinner 
		# and the position of it 
		size_hint: None, None
		size: 200, 50
		pos_hint:{'center_x':.5, 'top': 1} 

'''