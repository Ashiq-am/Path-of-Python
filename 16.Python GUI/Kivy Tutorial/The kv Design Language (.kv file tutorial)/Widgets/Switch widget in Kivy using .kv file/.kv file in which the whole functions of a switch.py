''''''


"""
# .kv file in which the whole functions of a switch 
# Along with labels are present 

<SimpleSwitch>: 

	# creating box layout for better view 
	BoxLayout: 
		size_hint_y: None
		height: '48dp'

		# Adding label to switch 
		Label: 
			text: 'Switch normal'

		# creating the switch 
		Switch: 

			# False means OFF and True means ON 
			active: False
			
			# Arranging a callback to the switch 
			on_active: root.switch_callback(self, self.active) 

	# Another for another switch 
	
	BoxLayout: 
		size_hint_y: None
		height: '48dp'

		Label: 
			text: 'Switch active'
		Switch: 
			active: True
			on_active: root.switch_callback(self, self.active) 


	BoxLayout: 
		size_hint_y: None
		height: '48dp'

		Label: 
			text: 'Switch off & disabled'
			
		Switch: 
			# disabled True means After making switch False 
			# it is disabled now you cannot change its state 
			disabled: True
			active: False

	BoxLayout: 
		size_hint_y: None
		height: '48dp'

		Label: 
			text: 'Switch on & disabled'
		Switch: 
			disabled: True
			active: True

"""