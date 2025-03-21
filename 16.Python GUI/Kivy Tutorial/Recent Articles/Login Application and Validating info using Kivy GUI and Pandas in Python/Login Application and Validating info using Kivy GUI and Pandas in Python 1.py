''''''

"""
# there are three screens 
windowManager: 
	loginWindow: 
	signupWindow: 
	logDataWindow: 

# GUI for the login window 
<loginWindow>: 
	email : email 
	pwd : pwd 
	FloatLayout: 
		size: root.width, root.height 
		Label: 
			text : "EMAIL: "
			size_hint : 0.2, 0.1
			pos_hint : {"x":0.25, "top":0.9} 
		TextInput: 
			id : email 
			multiline :False
			size_hint : 0.3, 0.1
			pos_hint : {"x" : 0.45, "top" : 0.9} 
		Label: 
			text : "PASSWORD: "
			size_hint : 0.2, 0.1
			pos_hint : {"x" : 0.25, "top" : 0.7} 
		TextInput: 
			id : pwd 
			multiline :False
			size_hint : 0.3, 0.1
			pos_hint : {"x" : 0.45, "top" : 0.7} 
		Button: 
			text : "Create an account"
			size_hint : 0.4, 0.1
			pos_hint : {"x" : 0.33, "top" : 0.4} 
			on_release: 
				app.root.current = 'signup'
				root.manager.transition.direction = "left"
		Button: 
			text : "LOGIN"
			size_hint : 0.3, 0.1
			pos_hint : {"x" : 0.39, "top" : 0.2} 
			on_release: 
				root.validate() 
				root.manager.transition.direction = "up"

# GUI for the signup window 
<signupWindow>: 
	name2 : name2 
	email : email 
	pwd : pwd 
	FloatLayout: 
		Label: 
			text : "NAME: "
			size_hint : 0.2, 0.1
			pos_hint : {"x":0.25, "top":0.9} 
		TextInput: 
			id : name2 
			multiline : False
			size_hint : 0.3, 0.1
			pos_hint : {"x" : 0.45, "top" : 0.9} 
		Label: 
			text : "EMAIL: "
			size_hint : 0.2, 0.1
			pos_hint : {"x" : 0.25, "top" : 0.7} 
		TextInput: 
			id : email 
			multiline : False
			size_hint : 0.3, 0.1
			pos_hint : {"x" : 0.45, "top" : 0.7} 
		Label: 
			text : "PASSWORD: "
			size_hint : 0.2, 0.1
			pos_hint : {"x" : 0.25, "top" : 0.5} 
		TextInput: 
			id : pwd 
			multiline : False
			size_hint : 0.3, 0.1
			pos_hint : {"x" : 0.45, "top" : 0.5} 
		Button: 
			text : "SUBMIT"
			size_hint : 0.3, 0.1
			pos_hint : {"x" : 0.39, "top" : 0.28} 
			on_press : 
				root.signupbtn() 
				root.manager.transition.direction = "right"

# GUI to show validation result 
<logDataWindow>: 
	info : info 
	FloatLayout: 
		Label: 
			id : info 
			size_hint : 0.8, 0.2
			pos_hint : {"x" : 0.15, "top" : 0.8} 
			text : "SUCCESSFULLY LOGGED IN"
		Button: 
			text : "Login"
			size_hint : 0.4, 0.1
			pos_hint : {"x" : 0.33, "top" : 0.55} 
			on_release: 
				app.root.current = 'login'
				root.manager.transition.direction = "down"
		Button: 
			text : "Create new account"
			size_hint : 0.4, 0.1
			pos_hint : {"x" : 0.33, "top" : 0.4} 
			on_release: 
				app.root.current = 'signup'
				root.manager.transition.direction = "down"


# GUI for pop up window 
<P>: 
	Label: 
		text : "Please enter valid information"
		size_hint : 0.2, 0.1
		pos_hint : {"x" : 0.3, "top" : 0.8} 


"""