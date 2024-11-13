import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

		# create parent panel for button
		self.pnl = wx.Panel(self)

		# create button at point (20, 20)
		self.btn = wx.Button(self.pnl, id = 1, label ="Button", pos =(20, 20),
											size =(300, 40), name ="button")

		# change foreground colour of button to blue
		self.btn.SetForegroundColour((0, 0, 255, 255))

		self.SetSize((350, 250))
		self.SetTitle('wx.Button')
		self.Centre()

def main():
	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
