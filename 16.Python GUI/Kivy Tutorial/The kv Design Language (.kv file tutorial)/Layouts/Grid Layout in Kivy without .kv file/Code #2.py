''''''
'""Now, let’s fix the size of Hello buttons to 100px instead of using size_hint_x=1"'


# creating the App class
class Grid_LayoutApp(App):

	# to build the application we have to
	# return a widget on the build() function.
	def build(self):

		# adding GridLayouts in App
		# Defining number of coloumn
		# You can use row as well depends on need
		layout = GridLayout(cols = 2)

		# 1st row
		layout.add_widget(Button(text ='Hello 1', size_hint_x = None, width = 100))
		layout.add_widget(Button(text ='World 1'))

		# 2nd row
		layout.add_widget(Button(text ='Hello 2', size_hint_x = None, width = 100))
		layout.add_widget(Button(text ='World 2'))

		# 3rd row
		layout.add_widget(Button(text ='Hello 3', size_hint_x = None, width = 100))
		layout.add_widget(Button(text ='World 3'))

		# 4th row
		layout.add_widget(Button(text ='Hello 4', size_hint_x = None, width = 100))
		layout.add_widget(Button(text ='World 4'))

		# returning the layout
		return layout
