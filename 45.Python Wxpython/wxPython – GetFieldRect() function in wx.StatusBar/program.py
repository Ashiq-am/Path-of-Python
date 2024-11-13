import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.statusbar = wx.StatusBar()
		self.statusbar.Create(self, id = 1, style = wx.STB_DEFAULT_STYLE,
													name = "Status Bar")

		self.SetStatusBar(self.statusbar)
		self.SetSize((350, 250))
		self.statusbar.SetFieldsCount(2)
		self.statusbar.SetStatusWidths([200, 1])
		self.statusbar.SetStatusText("Hi I am Status Bar")

		# GET wx.Rect OBJECT
		field = self.statusbar.GetFieldRect(1)

		# PRINT field
		print(field)

		self.SetTitle('New Frame Title')
		self.Centre()

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
