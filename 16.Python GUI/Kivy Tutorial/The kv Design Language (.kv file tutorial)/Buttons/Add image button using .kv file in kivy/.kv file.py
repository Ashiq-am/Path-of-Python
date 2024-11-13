""""""


'''
#.kv file implementation of seting position, size and functionality of btn 


# create a fully styled functional button 
# Adding images normal.png and down.png 
<Base>: 
	Button: 
		text: 'Hit me !!'
		background_normal: 'normal.png'
		background_down: 'down.png'
		size_hint: .3, .3
		pos_hint: {"x":0.35, "y":0.3} 
		on_press: root.say_hello() 

'''