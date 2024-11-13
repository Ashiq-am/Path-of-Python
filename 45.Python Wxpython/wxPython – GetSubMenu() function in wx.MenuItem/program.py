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
		self.st = wx.StaticText(self, label ="", pos =(20, 20), style = wx.ALIGN_LEFT)
		item = wx.MenuItem(fileMenu, 1, '&Check\tCtrl + c', helpString ="Check Help")
		item.SetSubMenu(sm)
		fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', sm)
		# get submenu
		s = item.GetSubMenu()
		# get total sub menu item
		n = s.MenuItemCount
		# print total sub menu item
		print(n)
		self.st.SetLabel(str(n)+" total submenu items")
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
