# Set Font
font = tkfont.Font(font=text['font'])

# Set Tab size
tab_size = font.measure('	 ')
text.config(tabs=tab_size)
