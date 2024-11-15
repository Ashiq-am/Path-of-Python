""""""


"""
#.kv file of main.py file 

#: import CheckBox kivy.uix.checkbox 

# giving colour to lable 
<CustLabel@Label>: 
	color: .761, .190, .810, 1

<SampBoxLayout>: 
	orientation: "vertical"
	padding: 10
	spacing: 10

	CustLabel: 
		text: "Gender"
		size_hint_x: 1
		font_size:20

	# creating box layout 
	BoxLayout: 
		# assigning orentation 
		orientation: "horizontal"
		height: 20

		BoxLayout: 
			orientation: "horizontal"
			size_hint_x: .22

			# label creation 
			CustLabel: 
				text: "Male"
				size_hint_x: .80
				font_size:30
			CheckBox: 
				color:.294, .761, .623
				on_active: root.checkbox_click(self, self.active) 
				size_hint_x: .20

			CustLabel: 
				text: "Female"
				size_hint_x: .80
				font_size:20
			CheckBox: 
				on_active: root.checkbox_click(self, self.active) 
				size_hint_x: .20

			CustLabel: 
				text: "Other"
				size_hint_x: .80
				font_size:10
			CheckBox: 
				on_active: root.checkbox_click(self, self.active) 
				size_hint_x: .20

"""