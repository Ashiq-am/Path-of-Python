import wx


class Example(wx.Frame):
    global count
    count = 0;

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        self.toolbar = self.CreateToolBar()

        # add tool using AddLabelTool() method
        qtool = self.toolbar.AddLabelTool(12, 'Quit',
                                          wx.Bitmap('/Desktop/wxPython/right.png'),
                                          kind=wx.ITEM_NORMAL,
                                          shortHelp="AddLabelTool")

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
