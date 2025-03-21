''''''


"""
# creating simple Pagelayout using.kv 

# creating page Layout 
<PageLayout>: 

	# Creating Page 1 
	
	# Using BoxLayout inside PageLayout 
	BoxLayout: 

		# creating Canvas 
		canvas: 
			Color: 
				rgb: 0, .5, .95, 1
			Rectangle: 
				pos: self.pos 
				size: self.size 

		# Providing orentation to the BoxLayout 
		orientation: "vertical"

		# creating Button 
		Button: 
			text: "Page 1"
			size_hint_y: .4

		# Adding Lable to Page 1 
			
		Label: 
			markup: True
			text: "GFG[b]:):):):)[/b]"
			color: 0, 0, 0, 1
			outline_color: 0, 0.5, 0.5, 1
			font_size: 30


	# Creating Page 2 
	BoxLayout: 
		orientation: "vertical"
		
		canvas: 
			Color: 
				rgba: 109 / 255., 8 / 255., 57 / 255., 1
			Rectangle: 
				pos: self.pos 
				size: self.size 
		Label: 
			markup: True
			text: " Kivy[b]PageLayout[/b]!!!!! "
			color: 0, 0, 0, 1
			outline_color: 0, 0.5, 0.5, 1
			font_size: 30

			
		Button: 
			text: "Page 2"
			size_hint_y: .2


	# Creating Page 3 
	BoxLayout: 
		
		orientation: 'vertical'

		canvas: 
			Color: 
				rgba: 100 / 555., 9 / 155., 37 / 455., 1
			Rectangle: 
				pos: self.pos 
				size: self.size 

		Label: 
			text: 'page 3'

		# This Image is directly from the websource 
		# By using AsyncImage you can use that 
		AsyncImage: 
			source: 'http://kivy.org / logos / kivy-logo-black-64.png'
		


	# Creating Page 4 
	Button: 
		# Adding image 
		# image must be .png 
		# and present at the same folder where 
		# .kv and main file is saved 
		Image: 
			source: "download.png"
			center_x: self.parent.center_x 
			center_y: self.parent.center_y 

"""