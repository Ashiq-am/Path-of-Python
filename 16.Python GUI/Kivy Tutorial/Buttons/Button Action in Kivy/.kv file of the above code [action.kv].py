''''''


'''

# Base widget from Rootwidget class in .py file 
<RootWidget>: 

	# used to change the label text 
	# as in rootwidget class 
	lbl:my_label 

	# child that is an instance of the BoxLayout 
	BoxLayout: 
		orientation: 'vertical'
		size: [1, .25] 

	Button: 
		text:'Click Me'
		font_size:"50sp"
		color: [0, 255, 255, .67] 
		on_press: root.btn_clk() 

	Label: 
		# id is limited in scope to the rule 
		# it is declared in. An id is a weakref 
		# to the widget and not the widget itself. 
		id: my_label 
		text: 'No click Yet'
		color: [0, 84, 80, 19] 


'''




"""Note: BoxLayout arranges widgets in either in a vertical fashion that is one on top of another 
or in a horizontal fashion that is one after another."""