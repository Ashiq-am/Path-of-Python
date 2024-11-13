from nicegui import ui

ui.label().set_text(text="This text is passed in set_text")

ui.label("Text visible or not").set_visibility(False)

ui.run()
