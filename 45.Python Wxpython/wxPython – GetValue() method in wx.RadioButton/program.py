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
        # create a parent panel for radio buttons
        self.pnl = wx.Panel(self)

        # create a radio buttons in frame
        self.rb1 = wx.RadioButton(self.pnl,
                                  label='Button 1',
                                  pos=(30, 10))
        self.rb2 = wx.RadioButton(self.pnl,
                                  label='Button 2',
                                  pos=(30, 30))
        self.rb3 = wx.RadioButton(self.pnl,
                                  label='Button 3',
                                  pos=(30, 50))

        # change value of second button to True
        self.rb2.SetValue(True)

        # print values of radio buttons True
        # if checked, False otherwise
        print(self.rb1.GetValue())
        print(self.rb2.GetValue())
        print(self.rb3.GetValue())


# main function
def main():
    # create a App object
    app = wx.App()
    # create a Example object
    ex = Example(None)

    ex.Show()

    # running a app
    app.MainLoop()


# Driver code
if __name__ == '__main__':
    # main function call
    main()
