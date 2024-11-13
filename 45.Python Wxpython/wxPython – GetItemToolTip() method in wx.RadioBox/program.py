import wx


class FrameUI(wx.Frame):

    def __init__(self, parent, title):
        super(FrameUI, self).__init__(parent, title=title, size=(300, 200))

        # function for in-frame components
        self.InitUI()

    def InitUI(self):
        # parent panel for radio box
        pnl = wx.Panel(self)

        # list of choices
        lblList = ['Radio One', 'Radio Two']

        # create radio boc containing above list
        self.rbox = wx.RadioBox(pnl, label='RadioBox', pos=(80, 10), choices=lblList,
                                majorDimension=1, style=wx.RA_SPECIFY_COLS)

        # set tooltip for first tool
        self.rbox.SetItemToolTip(0, "Item One")

        # create object for wx.ToolTip
        tip = self.rbox.GetItemToolTip(0)

        # print tooltip text associated with item index 0
        print(tip.GetTip())

        # set frame in centre
        self.Centre()
        # set size of frame
        self.SetSize((400, 250))
        # show output frame
        self.Show(True)


# wx App instance
ex = wx.App()
# Example instance
FrameUI(None, 'RadioButton and RadioBox')
ex.MainLoop()
