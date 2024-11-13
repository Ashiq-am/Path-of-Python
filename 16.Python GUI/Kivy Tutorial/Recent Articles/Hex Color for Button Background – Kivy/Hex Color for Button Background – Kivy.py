# importing button widget from kivy framework
from kivy.uix.button import Button

from kivy.app import App

# importing builder from kivy
from kivy.lang import Builder


# this is the main class which will
# render the whole application
class uiApp(App):

    # method which will render our application
    def build(self):
        return Builder.load_string(""" 

#:import C kivy.utils.get_color_from_hex 
Button: 

# text which will appear on first button 
text:"first button" 

background_color: C("#f9f871") 
								""")

    # running the application


uiApp().run()
