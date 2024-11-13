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

        # Radio tool using AddTool() Function
        ptool = self.toolbar.AddTool(12, 'oneTool',
                                     wx.Bitmap('/home/wxPython/right.png'),
                                     wx.Bitmap('/home/wxPython/wrong.png'),
                                     kind=wx.ITEM_RADIO, shortHelp="Simple Tool")

        spc = self.toolbar.AddStretchableSpace()

        # Check tool using AddTool() Function
        qtool = self.toolbar.AddTool(12, 'oneTool', wx.Bitmap('/home/wxPython/right.png'),
                                     wx.Bitmap('/home/wxPython/wrong.png'),
                                     kind=wx.ITEM_CHECK, shortHelp="Simple Tool")

        spc = self.toolbar.AddStretchableSpace()
        # Normal tool using AddTool() Function
        rtool = self.toolbar.AddTool(12, 'oneTool', wx.Bitmap('/home/wxPython/right.png'),
                                     wx.Bitmap('/home/wxPython/wrong.png'),
                                     kind=wx.ITEM_NORMAL, shortHelp="Simple Tool")

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
