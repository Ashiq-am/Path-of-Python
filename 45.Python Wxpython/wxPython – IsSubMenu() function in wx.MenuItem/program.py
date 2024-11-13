import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()

        sm = wx.Menu()
        sm.Append(wx.ID_ANY, 'Submenu item 1')
        sm.Append(wx.ID_ANY, 'Submenu item 2')
        sm.Append(wx.ID_ANY, 'Submenu item 3')
        item = wx.MenuItem(fileMenu, 1, '&Check\tCtrl + c', helpString="Check Help")
        item.SetSubMenu(sm)
        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', sm)

        n = item.IsSubMenu()
        # if item is sub menu
        if (n == True):
            print("Item is SubMenu Item")
        else:
            print("Item is not a SubMenu Item")
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle('Submenu')
        self.Centre()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
