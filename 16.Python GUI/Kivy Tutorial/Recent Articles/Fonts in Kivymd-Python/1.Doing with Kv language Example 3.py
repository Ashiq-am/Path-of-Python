# app class
class Test(MDApp):
    def build(self):
        # this will load kv lang
        screen = Builder.load_string(KV)

        # running loop for all the declared font name
        for font_name in [
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
            screen.ids.box.add_widget(
                MDLabel(
                    text="GEEKSFORGEEKS",
                    halign="center",
                    font_style=font_name,
                )
            )
        # returning screen
        return screen


# running app
Test().run()
