import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.item = wx.MenuItem(self.fileMenu, 1, '&Check\tCtrl + c', helpString ="Check Help")
		self.item.SetMarginWidth(12)
		self.st = wx.StaticText(self, label ="", pos =(20, 20), style = wx.ALIGN_LEFT)
		self.fileMenu.Append(self.item)
		self.menubar.Append(self.fileMenu, '&File')
		self.SetMenuBar(self.menubar)
		# menu object
		menu = self.item.GetMenu()
		# print title of menu
		print(menu.Title)
		self.st.SetLabel(menu.Title)
		self.SetSize((350, 250))
		self.SetTitle('')
		self.Centre()


def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
