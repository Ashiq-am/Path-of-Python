# importing the modules
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# this class is used as a Base for our
# Root Widget which is LoginScreen
class LoginScreen(GridLayout):

	# overriding the method __init__() so as to
	# add widgets and to define their behavior
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)

		# GridLayout managing its children in two columns
		# and add a Label and a TextInput for the Email id and password
		self.cols = 2
		self.add_widget(Label(text = 'Email id'))
		self.username = TextInput(multiline = False)
		self.add_widget(self.username)
		self.add_widget(Label(text = 'password'))
		self.password = TextInput(password = True, multiline = False)
		self.add_widget(self.password)

class MyApp(App):
	def build(self):
		return LoginScreen()


if __name__ == '__main__':

	# MyApp is initialized and
	# its run() method called
	MyApp().run()
