# importing packages
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout


# defining MainApp class
class MainApp(MDApp):
    def build(self):
        # this will set MDBoxLayout to vertical
        screen = MDBoxLayout(orientation='vertical')

        # running loop for all the declared font name
        for name_theme in [
            "H1",
            "H2",
            "Subtitle1",
            "Button",
            "Overline",
            "Caption",
            "Icon",
        ]:  # this will add widgets to the screen
            # for all font_name
            # declared in list
            screen.add_widget(
                MDLabel(
                    text="GEEKSFORGEEKS",
                    halign="center",
                    font_style=name_theme,
                )
            )

        # returing screen
        return screen


# running app
MainApp().run()
