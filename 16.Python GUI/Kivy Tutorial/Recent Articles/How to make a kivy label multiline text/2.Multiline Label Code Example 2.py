import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyDemoApp(App):
	def build(self):
		ll = Label(text="GeeksForGeeks is the \nbest platform for \nDSA content")
		return ll

label = MyDemoApp()

label.run()
