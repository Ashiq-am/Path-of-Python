import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.statusbar = wx.StatusBar()
        self.statusbar.Create(self, id=1, style=wx.STB_DEFAULT_STYLE,
                              name="Status Bar")
        self.SetStatusBar(self.statusbar)
        self.SetSize((350, 250))

        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([150, 150])
        self.statusbar.SetStatusText("This is text after stack pop in field 1", 0)
        self.statusbar.SetStatusText("This is text after stack pop in field 2", 1)
        self.statusbar.SetStatusStyles(styles=[wx.SB_RAISED, wx.SB_SUNKEN])

        # PUSH TEXT IN STATUS TEXT STACK
        self.statusbar.PushStatusText(string="This is pushed text for field 1", field=0)
        self.statusbar.PushStatusText(string="This is pushed text for field 2", field=1)

        # POP TEXT IN STATUS TEXT STACK
        self.statusbar.PopStatusText(field=0)

        self.statusbar.PopStatusText(field=1)
        self.SetTitle('New Frame Title')
        self.Centre()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
