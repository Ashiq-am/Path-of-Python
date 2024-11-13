from nicegui import ui

ui.label().set_text(text="This text is passed in set_text.")

# visibility is set to False
ui.icon("lock",color="green",size="50px").set_visibility(False)

ui.run()
