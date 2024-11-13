# importing kivy App
from kivy.app import App

# importing BoxLayout from kivy
from kivy.uix.boxlayout import BoxLayout

# importing ScreenManager and Screen from kivy
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(BoxLayout):
    pass


class uiApp(App):
    def on_start(self):
        from kivy.base import EventLoop

        # attaching keyboard hook when app starts
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):

        # key == 27 means it is waiting for
        # back button tobe pressed
        if key == 27:

            # checking if we are at mainscreen or not
            if self.screen_manager.current == 'mainscreen':

                # return True means do nothing
                return True
            else:

                # return anything except True result in
                # closing of the app on button click
                # if are not at mainscreen and if we press
                # back button the app will get terminated
                pass

    def build(self):
        self.screen_manager = ScreenManager()

        # adding Designed screen to ScreenManager
        self.mainscreen = MainWindow()
        screen = Screen(name='mainscreen')
        screen.add_widget(self.mainscreen)
        self.screen_manager.add_widget(screen)

        # returning screen manager
        return self.screen_manager


if __name__ == "__main__":
    # running the object of app
    uiApp().run()
