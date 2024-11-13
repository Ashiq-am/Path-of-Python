# importing wx library
import wx

APP_EXIT = 1


# create a Example class
class Example(wx.Frame):
    # constructor
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        # method calling
        self.InitUI()

    # method for user interface creation
    def InitUI(self):
        # parent panel for radio buttons
        self.pnl = wx.Panel(self)

        # create radio buttons
        self.rb1 = wx.RadioButton(self.pnl,
                                  label='Button 1',
                                  pos=(30, 10))
        self.rb2 = wx.RadioButton(self.pnl,
                                  label='Button 2',
                                  pos=(30, 30))
        self.rb3 = wx.RadioButton(self.pnl,
                                  label='Button 3',
                                  pos=(30, 50))

        # set value for the second radio button as true(checked)
        self.rb2.SetValue(True)


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
