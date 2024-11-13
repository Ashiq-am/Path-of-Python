# importing wx library
import wx

APP_EXIT = 1


# create an Example class
class Example(wx.Frame):
    # constructor
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        # method calling
        self.InitUI()

    # method for user interface creation
    def InitUI(self):
        # create parent panel in frame for radio button
        self.pnl = wx.Panel(self)

        # initialize radio button
        self.rb = wx.RadioButton()

        # create radio button with two step creation
        self.rb.Create(self.pnl, id=1,
                       label="Radio",
                       pos=(20, 20))


# main function
def main():
    # create an App object
    app = wx.App()

    # create an Example object
    ex = Example(None)
    ex.Show()

    # running an app
    app.MainLoop()

# Driver code
if __name__ == '__main__':
    # main function call
    main()
