import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.statusbar = wx.StatusBar()
		self.statusbar.Create(self, id = 1, name = "Status Bar")
		self.SetStatusBar(self.statusbar)
		self.SetSize((350, 250))

		# SET TOTAL NUMBER OF FIELDS AND RESPECTIVE WIDTHS
		self.statusbar.SetFieldsCount(3, [100, 80, 60])

		# SET TEXT FOR ALL FIELDS
		self.statusbar.SetStatusText("Field One", 0)
		self.statusbar.SetStatusText("Field Two", 1)
		self.statusbar.SetStatusText("Field Three", 2)
		self.statusbar.SetBackgroundColour((200, 188, 73, 243))

		# SET STYLES FOR ALL STATUS FIELDS
		self.statusbar.SetStatusStyles([wx.SB_FLAT, wx.SB_SUNKEN, wx.SB_RAISED])
		self.SetTitle('New Frame Title')
		self.Centre()
		print(self.statusbar.GetMinHeight())


def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
