''''''


"""
# .kv file of the popup code 

# Adding Button widget 
<Widgets>: 
	Button: 
		text: "Press me"
		on_release: root.btn() 

# Adding Label, Button to popup 
<Popups>: 
	
	Label: 
		text: "You pressed the button"
		size_hint: 0.6, 0.2
		pos_hint: {"x":0.2, "top":1} 

	Button: 
		text: "Close the popup"
		# set size of the button 
		size_hint: 1, 0.4
		# set position of the button 
		pos_hint: {"x":0, "y":0.1} 

"""