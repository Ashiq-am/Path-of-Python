""""""


'''
#.kv file implementation of seting position and size of btn 
<FloatLayout>: 
		
	Button: 
		text: "pos_hint "
		background_color: 0.1, 0.5, 0.6, 1

		# Giving size hint i.e size of button is 
		# 30 % by hight and width of layout . 
		size_hint: 0.3, 0.3
		
		# positioned at 0 % right and 100 % up / top 
		# from botton left, i.e x, top = 0, 100 from bottom left: 
		pos_hint: {"x":0, "top":1} 
	
			
	Button: 
		text:"pos"
		background_color: 0.4, 0.5, 0.6, 1
		size_hint: 0.3, 0.3
		pos: 100, 100
	
	Button: 
		text:"size_hint"
		background_color: 0, 0, 1, 1

		# Giving size hint i.e size of button is 
		# 40 % by hight and 50 % width of layout . 
		size_hint: 0.5, 0.4
		pos_hint: {"x":.4, "top":1} 

					

'''