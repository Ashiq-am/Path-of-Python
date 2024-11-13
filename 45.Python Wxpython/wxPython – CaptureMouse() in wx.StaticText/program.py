# importing wx library
import wx


# create an Example class
class Example(wx.Frame):

    # constructor
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        # method calling
        self.InitUI()

    # method for user interface creation
    def InitUI(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        # create parent panel
        self.pnl = wx.Panel(self)

        # create static text at point (20,20)
        self.st = wx.StaticText(self.pnl, id=1,
                                label="StaticText",
                                pos=(20, 20))

        # capture mouse on static text
        self.st.CaptureMouse()

        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Centre()


# main function
def main():
    # create an App object
    app = wx.App()

    # create an Example object
    ex = Example(None)
    ex.Show()

    # running a app
    app.MainLoop()

# Driver code
if __name__ == '__main__':
    # main function call
    main()
