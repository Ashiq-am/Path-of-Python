import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        # create parent panel
        self.pnl = wx.Panel(self)

        # create a button at point (20, 50)
        self.btn1 = wx.Button(self.pnl, id=1, label="Remove Text", pos=(20, 50))

        # create button to destroy
        self.btn0 = wx.Button(self.pnl, id=1, label="Click button to remove", pos=(20, 20))

        # bind Onclick() function with button
        self.btn1.Bind(wx.EVT_BUTTON, self.Onclick)

        self.SetSize((350, 250))
        self.SetTitle('wx.Button')
        self.Centre()

    def Onclick(self, e):
        # destroy btn0 button
        self.btn0.Destroy()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
