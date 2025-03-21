import wx


class Example(wx.Frame):

	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw)

		# create MenuBar using MenuBar() function
		menubar = wx.MenuBar()

		# add menu to MenuBar
		fm1 = wx.Menu()
		fileitem = fm1.Append(20, "one")

		fm2 = wx.Menu()
		fileitem2 = fm2.Append(21, "two")
		menubar.Append(fm1, '&Menu_one')
		menubar.Append(fm2, '&Menu_two')
		self.SetMenuBar(menubar)
		self.SetSize((300, 200))
		self.SetTitle('Menu Bar')

		# STATIC TEXT WITH LABEL OF MENU AT POSITIO 1
		st1 = wx.StaticText(self, label = menubar.GetMenuLabel(1),
											style = wx.ALIGN_LEFT)

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
