import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyDemoApp(App):
	def build(self):
		ll = Label(text="This is a\nmultiline\nlabel")
		return ll

label = MyDemoApp()

label.run()
