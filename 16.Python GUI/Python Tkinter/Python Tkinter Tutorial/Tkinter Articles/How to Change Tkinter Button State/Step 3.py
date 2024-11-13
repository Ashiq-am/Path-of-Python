# Helper function which will change the State of Button1
def changeState(self) -> None:
    # Printing the State of
    # the Button before ALTERING it
    # This is optional
    print(self.button1['state'])

    # Checking if the STATE of the Button1

    # If the STATE is NORMAL
    if (self.button1['state'] == NORMAL):

        # Change the state to DISABLED
        self.button1['state'] = DISABLED
    else:

        # Otherwise, change the state to NORMAL
        self.button1['state'] = NORMAL
