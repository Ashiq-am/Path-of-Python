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
        # create parent panel for radio buttons
        self.pnl = wx.Panel(self)

        # create radio button
        self.rb = wx.RadioButton()
        self.rb.Create(self.pnl, id=1,
                       label="Radio",
                       pos=(20, 20))

        # set background colour to blue
        self.rb.SetBackgroundColour((0, 0,
                                     255, 255))
        # set foreground colour to white
        self.rb.SetForegroundColour((255, 255,
                                     255, 255))

        # create wx.VisualAttributes object
        v = self.rb.GetClassDefaultAttributes()

        # print background colour
        print(v.colBg)
        # print foreground colour
        print(v.colFg)


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
