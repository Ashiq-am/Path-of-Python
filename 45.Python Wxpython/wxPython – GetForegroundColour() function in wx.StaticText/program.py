# importing the module
import wx


# definition of the Example class
class Example(wx.Frame):

    # instantiating the class
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    # method for creation of user interface
    def InitUI(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        # create parent panel for button
        self.pnl = wx.Panel(self)

        # create button at point (20, 20)
        self.st = wx.StaticText(self.pnl, id=1, label="Button")

        # change foreground colour of button
        self.st.SetForegroundColour((10, 20, 255, 255))

        # get foreground colour
        fc = self.st.GetForegroundColour()

        # print foreground colour
        print(fc)

        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Centre()


# definition of the main function
def main():
    # creating an App object
    app = wx.App()

    # creating an Example object
    ex = Example(None)

    # showing the Example object
    ex.Show()

    # running the App object
    app.MainLoop()


# driver code
if __name__ == '__main__':
    main()
