import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):
		# CREATE FONT
		fnt = wx.Font(pointSize = 8, family = wx.FONTFAMILY_MODERN, style = wx.FONTSTYLE_ITALIC, weight = wx.FONTWEIGHT_BOLD)
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.item = wx.MenuItem(self.fileMenu, 1, '&Radio', helpString ="Check Help", kind = wx.ITEM_CHECK)
		# SET FONT FOR MENU ITEM self.item
		self.item.SetFont(fnt)
		self.item.Enable(False)
		self.fileMenu.Append(self.item)
		self.menubar.Append(self.fileMenu, '&File')
		self.SetMenuBar(self.menubar)
		self.SetSize((350, 250))
		self.SetTitle('Icons and shortcuts')
		self.Centre()

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
