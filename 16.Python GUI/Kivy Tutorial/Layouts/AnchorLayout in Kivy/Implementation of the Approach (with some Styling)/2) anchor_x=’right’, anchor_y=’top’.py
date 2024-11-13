# A Kivy app demonstrating the working of anchor layout
from sl import App


class AnchorLayoutApp(App):

    def build(self):
        # Anchor Layout1
        layout = AnchorLayout(
            anchor_x='right', anchor_y='top')
        btn = Button(text='Hello World',
                     size_hint=(.3, .3),
                     background_color=(1.0, 0.0, 1.0, 1.0))

        layout.add_widget(btn)
        return layout

