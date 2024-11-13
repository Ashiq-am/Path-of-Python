import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitUI()

	def InitUI(self):

		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.statusbar = wx.StatusBar()
		self.statusbar.Create(self, id = 1,
							style = wx.STB_DEFAULT_STYLE,
							name = "Status Bar")
		self.SetStatusBar(self.statusbar)
		self.SetSize((350, 250))

		# Get wx.VisualAttributes object
		va = self.statusbar.GetClassDefaultAttributes(variant = wx.WINDOW_VARIANT_NORMAL)

		# Print Background Colour
		print(va.colBg)
		# Print Fore Ground Colour
		print(va.colFg)
		# Print Identifier for font family
		print(va.font.Family)
		self.SetTitle('New Frame Title')
		self.Centre()

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
