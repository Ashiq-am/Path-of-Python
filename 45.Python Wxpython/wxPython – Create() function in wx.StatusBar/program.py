import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		# INITIALIZE USING EMPTY CONSTRUCTOR
		self.statusbar = wx.StatusBar()
		# CREATE STATUS BAR USING CREATE FUNCTION
		self.statusbar.Create(self, id = 1, style = wx.STB_DEFAULT_STYLE,
													name = "Status Bar")
		self.statusbar.SetStatusText("Hello there this is a Status Bar")
		self.SetStatusBar(self.statusbar)
		self.SetSize((350, 250))
		self.SetTitle('New Frame Title')
		self.Centre()

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
