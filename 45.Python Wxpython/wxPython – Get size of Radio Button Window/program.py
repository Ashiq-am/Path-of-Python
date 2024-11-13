import wx

APP_EXIT = 1


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        self.pnl = wx.Panel(self)

        # create radio button at position (30, 10)
        self.rb1 = wx.RadioButton(self.pnl, label='Btn1',
                                  pos=(30, 10), size=(100, 20))

        # change background colour
        self.rb1.SetBackgroundColour((255, 100, 255, 255))

        # change size to (300, 50)
        self.rb1.SetSize((300, 50))

        # print size of radio button
        print(self.rb1.GetSize())


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
