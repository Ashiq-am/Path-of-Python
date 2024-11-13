import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		# create toolbar using CreateToolBar function
		toolbar = self.CreateToolBar()
		qtool = toolbar.AddTool(wx.ID_ANY, 'Welcome', wx.Bitmap('/Desktop/wxPython/images.png'))
		toolbar.Realize()

		self.SetSize((600, 400))
		self.SetTitle('Simple toolbar')
		self.Centre()

	def OnQuit(self, e):
		self.Close()


def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
