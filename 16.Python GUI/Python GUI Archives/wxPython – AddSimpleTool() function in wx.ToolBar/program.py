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

        # Add Tool using AddSimpleTool() function
        ptool = self.toolbar.AddSimpleTool(12, wx.Bitmap('/home/wxPython/right.png'),
                                           shortHelpString="Simple Tool")
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
