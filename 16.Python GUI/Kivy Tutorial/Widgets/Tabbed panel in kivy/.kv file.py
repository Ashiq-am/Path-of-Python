''''''



"""
# .kv file of tabbed panel 

<Tab>: 

	# creating the size 
	# and the alignment of the tab 
	size_hint: .5, .5
	pos_hint: {'center_x': .5, 'center_y': .5} 
	do_default_tab: False

	# Create tab 1 
	TabbedPanelItem: 
		text: 'Tab 1'
		Label: 
			text: "First tab"

	# Create 2nd tab 
	TabbedPanelItem: 
		text: 'Tab 2'
		BoxLayout: 
			Label: 
				text: 'Press button'
			Button: 
				text: 'Click it'

	# Create 3rd tab 
	TabbedPanelItem: 
		text: 'Tab 3'
		RstDocument: 
			text: '\n'.join(("How are you GFG's???")) 


"""