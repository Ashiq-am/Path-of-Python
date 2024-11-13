# Creating App class which
# will contain our overall App
class App:
    def __init__(self, master) -> None:
        # Instantiating master i.e toplevel Widget
        self.master = master

        # Creating label
        self.label = Label(self.master,
                           text="Click Button2 to change Button1 State")
        self.label.pack(pady=10)

        # Creating button1
        # We will change the state of this Button
        # it has a initial state of "NORMAL"
        # i.e Button can be pressed
        self.button1 = Button(self.master,
                              text="Button1",
                              state=NORMAL)

        self.button1.pack(pady=20)

        # Creating another button
        # We will use this button to
        # change the State of first button
        self.button2 = Button(self.master,
                              text="Button2",
                              command=self.changeState)

        self.button2.pack(pady=20)
