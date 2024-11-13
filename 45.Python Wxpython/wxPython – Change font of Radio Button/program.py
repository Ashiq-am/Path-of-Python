import wx

APP_EXIT = 1


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        # create parent panel for radio buttons
        self.pnl = wx.Panel(self)

        # create radio buttons
        self.rb1 = wx.RadioButton(self.pnl, label='Btn1', pos=(30, 10), size=(100, 20))
        self.rb2 = wx.RadioButton(self.pnl, label='Btn2', pos=(30, 30), size=(100, 20))
        self.rb3 = wx.RadioButton(self.pnl, label='Btn3', pos=(30, 50), size=(100, 20))

        # declare font for radio buttons
        font = wx.Font(12, wx.FONTFAMILY_MODERN, 0, 90, underline=False,
                       faceName="")

        # set font for all radio buttons
        self.rb1.SetFont(font)
        self.rb2.SetFont(font)
        self.rb3.SetFont(font)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
