import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        # create parent panel
        self.pnl = wx.Panel(self)

        # create statictext at point (20, 20)
        self.st = wx.StaticText(self.pnl, id=1, label="Button")

        # change background colour of statictext
        self.st.SetBackgroundColour((10, 20, 255, 255))

        # get background colour
        bc = self.st.GetBackgroundColour()

        # print background colour
        print(bc)

        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Centre()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
