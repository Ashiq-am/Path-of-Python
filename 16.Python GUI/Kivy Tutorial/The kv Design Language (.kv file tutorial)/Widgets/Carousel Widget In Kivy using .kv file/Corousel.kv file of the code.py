""""""


"""
# Corousel.kv file of the code 

# Corousel Creation 
<Corousel>: 

	rows: 2

	# It shows the id which is different for different pages 
	Label: 
		text: str(id(root)) 

	# This button will take you directly to the 3rd page	 
	Button 
		text: 'load(page 3)'
		on_release: 
			carousel = root.parent.parent 
			carousel.load_slide(carousel.slides[2]) 

	# load_previous() is used to go back to previous page 
	Button 
		text: 'prev'
		on_release: 
			root.parent.parent.load_previous() 

	# load_next() is used to go to nevt page 
	Button 
		text: 'next'
		on_release: 
			root.parent.parent.load_next() 

"""