''''''

'''

# import the modules
from kivy.app import App
from kivy.uix.label import Label

# defining the Base Class of our first Kivy App
class MyApp(App):

	def build(self):

		# initializing a Label with text ‘Hello World’
		and return its instance
		return Label(text = 'welcome to GeeksforGeeks')


if __name__ == '__main__':
	# MyApp is initialized and its run() method called
	MyApp().run()
	
'''
