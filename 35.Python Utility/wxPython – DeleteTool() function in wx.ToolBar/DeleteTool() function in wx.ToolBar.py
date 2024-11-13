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
        self.ptool = self.toolbar.AddTool(12,
                                          'oneTool',
                                          wx.Bitmap('path/ wxPython / right.png'),
                                          shortHelp="Simple Tool")
        self.ptool = self.toolbar.AddTool(13,
                                          'oneTool',
                                          wx.Bitmap('path / wxPython / wrong.png'),
                                          shortHelp="Simple Tool")

        self.btn = wx.Button(pnl, label='Delete', pos=(20, 20))

        self.btn.Bind(wx.EVT_BUTTON, self.Onclick)
        self.toolbar.Realize()
        self.SetSize((350, 250))
        self.SetTitle('Control')
        self.Centre()

    def Onclick(self, e):
        # delete tool using DeleteTool() function
        self.toolbar.DeleteTool(12)


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
