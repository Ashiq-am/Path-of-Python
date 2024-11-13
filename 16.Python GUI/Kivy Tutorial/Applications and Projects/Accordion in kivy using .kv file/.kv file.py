''''''


"""
# .kv file of the Accordion App file 

# Allow style to image 
<MyImage@Image>: 
	keep_ratio: False
	allow_stretch: True

# Use the different image to show usage of accordian 
<Accor>: 
	orientation: 'vertical'
	AccordionItem: 
		title: 'HTML 5'
		MyImage: 
			source: 'html.png'
	AccordionItem: 
		title: 'CSS 3'
		MyImage: 
			source: 'css.png'
	AccordionItem: 
		title: 'JAVASCRIPT'
		MyImage: 
			source: 'javascript.png'
	AccordionItem: 
		title: 'NODE-JS'
		MyImage: 
			source: 'node-js.png'
	AccordionItem: 
		title: 'BOOTSTRAP'
		MyImage: 
			source: 'bootstrap.png'

"""