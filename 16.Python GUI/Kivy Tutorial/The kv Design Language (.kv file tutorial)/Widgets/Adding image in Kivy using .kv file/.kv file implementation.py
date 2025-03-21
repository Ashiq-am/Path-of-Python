""""""


'''
# How to use images in kivy using .kv 

# root widget od Imagekv Calss 
<Imagekv>: 

	# Giving orentation to Box Layout 
	orientation:'vertical'

############################################### 

	# Adding Box Layoyt 
	BoxLayout: 
		
		padding:5

		# Adding image from the system 
		Image: 
			source: 'download.jpg'

			# Giving the size of image 
			size_hint_x: 0.4

			# allow sterching of image 
			allow_stretch: True
			
		# Giving Label to images 
		Label: 
			text:"Python"
			font_size:11
			bold:True

		Label: 
			text:"Programing Language"
			font_size:10
			
############################################### 

# Drawing the line between the multiples 
	Label: 
		canvas.before: 
			Color: 
				rgba: (1, 1, 1, 1) 
			Rectangle: 
				size: self.size 
				pos: self.pos 
		size_hint_y: None
		height: 1

################################################ 

	# Another Box Layout 
	BoxLayout: 
		padding:5
		Image: 
			source:"downloadimg.jpg"
			size_hint_x: 0.4
			allow_stretch: True

		Label: 
			text:"Image"
			font_size:11
			bold:True

		Label: 
			text:"Python Image"
			font_size:10
			
############################################# 

	# Drawing the line between the multiples 
	Label: 
		canvas.before: 
			Color: 
				rgba: (1, 1, 1, 1) 
			Rectangle: 
				size: self.size 
				pos: self.pos 
		size_hint_y: None
		height: 1
		
############################################### 

	# Adding next Box Layout 
	BoxLayout: 
		padding:5

		# To load an image asynchronously 
		# (for example from an external webserver) 
		AsyncImage: 
			source: 'http://kivy.org/logos/kivy-logo-black-64.png'
			width: 100
			allow_stretch: True

		Label: 
			text:" Asynchronous Image "
			font_size:11
			bold:True

		Label: 
			text:"Kivy Logo"
			font_size:10

#################################################### 
			
	# Drawing the line between the multiples 
	Label: 
		canvas.before: 
			Color: 
				rgba: (1, 1, 1, 1) 
			Rectangle: 
				size: self.size 
				pos: self.pos 
		size_hint_y: None
		height: 1

##################################################### 

	# LAst Box Layout 
	BoxLayout: 
		padding:5
		
		AsyncImage: 
			size_hint_y: None
			source: 'http://kivy.org/slides/kivypictures-thumb.jpg'
			width: 100
			allow_stretch: True

		Label: 
			text:"Asynchronous Image "
			font_size:11
			bold:True

		Label: 
			text:" Webserver image "
			font_size:10

'''