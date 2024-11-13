import wx

APP_EXIT = 1


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        self.pnl = wx.Panel(self)

        # create radio button at position (30, 10)
        self.rb1 = wx.RadioButton(self.pnl, label='Btn1', pos=(30, 10), size=(100, 20))

        # create button
        self.btn = wx.Button(self.pnl, label='Btn1',
                             pos=(30, 50), size=(100, 20))

        # hide radio button
        self.rb1.Hide()

        # bind event function
        self.btn.Bind(wx.EVT_BUTTON, self.Onclick)

    def Onclick(self, e):
        # show hidden radio button
        self.rb1.Show()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
