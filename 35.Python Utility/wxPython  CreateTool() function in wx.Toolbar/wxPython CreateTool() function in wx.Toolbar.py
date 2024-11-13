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
        # create a tool using CreateTool() function
        self.ptool = self.toolbar.CreateTool(12,
                                             'oneTool',
                                             wx.Bitmap('path / wxPython / right.png'),
                                             shortHelp="Simple Tool")

        self.btn = wx.Button(pnl, label='Add created tool', pos=(20, 20))

        self.btn.Bind(wx.EVT_BUTTON, self.Onclick)
        self.toolbar.Realize()
        self.SetSize((350, 250))
        self.SetTitle('Control')
        self.Centre()

    def Onclick(self, e):
        # Add toolbar tool using AddTool() function
        self.toolbar.AddTool(self.ptool)
        self.btn.SetLabel("Added tool")


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
