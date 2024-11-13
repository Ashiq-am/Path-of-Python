import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.pnl = wx.Panel(self)
        font = wx.Font(10, family=wx.FONTFAMILY_MODERN, style=0, weight=90,
                       underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)

        self.btn = wx.Button(self.pnl, id=1, label="Click", pos=(20, 20),
                             size=wx.DefaultSize, name="statictext")
        self.btn.SetFont(font)

        # SET BACKGROUND COLOUR
        self.btn.SetBackgroundColour((255, 230, 200, 255))
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
