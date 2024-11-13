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

        qtool = self.toolbar.AddTool(12, 'right', wx.Bitmap('/home/wxPython/right.png'),
                                     shortHelp="Radio Tool")
        self.toolbar.AddSeparator()
        rtool = self.toolbar.AddTool(13, 'right2', wx.Bitmap('/home/wxPython/wrong.png'),
                                     shortHelp="Radio Tool")

        self.toolbar.Realize()
        self.SetSize((350, 250))
        self.SetTitle('Control')
        self.Centre()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
