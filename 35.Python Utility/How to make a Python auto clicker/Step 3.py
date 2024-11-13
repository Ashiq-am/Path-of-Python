# threading.Thread is used
# to control clicks
class ClickMouse(threading.Thread):

    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
