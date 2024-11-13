import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyDemoApp(App):
	def build(self):
		ll = Label(text='''Kivy is an open source software library 
						\nfor the rapid development of applications 
						\nequipped with novel user interfaces, 
						\nsuch as multi-touch apps.''')
		return ll

label = MyDemoApp()

label.run()
