# App class
class Test(MDApp):

    def build(self):
        # this will load kv lang
        screen = Builder.load_string(KV)

        # returning screen
        return screen


# running app
Test().run()
