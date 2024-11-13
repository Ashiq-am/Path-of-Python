import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.statusbar = wx.StatusBar(self, id = 1,
			style = wx.STB_DEFAULT_STYLE, name ="sb")
		self.statusbar.SetStatusText("This is StatusBar")
		self.statusbar.SetBackgroundColour((80, 60, 170, 230))

		self.SetStatusBar(self.statusbar)

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
