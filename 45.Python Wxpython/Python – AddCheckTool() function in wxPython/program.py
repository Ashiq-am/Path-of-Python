import wx


class Example(wx.Frame):
    global count
    count = 0

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        self.toolbar = self.CreateToolBar()

        # create check toolusing AddCheckTool() function
        rtool = self.toolbar.AddCheckTool(12, 'CheckTool',
                                          bitmap1=wx.Bitmap('/Desktop/wxPython/right.png'),
                                          bmpDisabled=wx.Bitmap('/Desktop/wxPython/wrong.png'))

        self.toolbar.Realize()

        self.SetSize((350, 250))
        self.SetTitle('Simple toolbar')
        self.Centre()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
