# importing button widget from kivy framework
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.window import Window

# importing builder from kivy
from kivy.lang import Builder


# this is the main class which
# will render the whole application
class uiApp(App):

    # method which will render our application
    def close_application(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()

    def build(self):
        return Builder.load_string(""" 

#:import C kivy.utils.get_color_from_hex 
Button: 

# text which will appear on first button 

text:"Close App" 
on_release: app.close_application() 

								""")

    # running the application


uiApp().run()
