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
        ptool = self.toolbar.AddTool(12, 'oneTool', wx.Bitmap('/home/wxPython/right.png'), shortHelp="Simple Tool")
        qtool = self.toolbar.AddTool(12, 'oneTool', wx.Bitmap('/home/wxPython/right.png'), shortHelp="Simple Tool")
        rtool = self.toolbar.AddTool(12, 'oneTool', wx.Bitmap('/home/wxPython/right.png'), shortHelp="Simple Tool")
        self.btn = wx.Button(pnl, label='Clear Tools', pos=(20, 20))

        self.btn.Bind(wx.EVT_BUTTON, self.Onclick)
        self.toolbar.Realize()
        self.SetSize((350, 250))
        self.SetTitle('Control')
        self.Centre()

    def Onclick(self, e):
        # clear tools using ClearTools() function
        self.toolbar.ClearTools()
        self.btn.SetLabel("Cleared")


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
