import wx

class PopMenu(wx.Menu):

	def __init__(self, parent):
		super(PopMenu, self).__init__()

		self.parent = parent

		# menu item 1
		popmenu = wx.MenuItem(self, wx.NewId(), 'one ')
		self.Append(popmenu)
		# menu item 2
		popmenu2 = wx.MenuItem(self, wx.NewId(), 'two')
		self.Append(popmenu2)

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

		self.SetSize((600, 400))
		self.SetTitle('Popup Menu')
		self.Centre()

	def OnRightDown(self, e):
		# sow popu menu
		self.PopupMenu(PopMenu(self), e.GetPosition())


def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
