import wx


class FrameUI(wx.Frame):

	def __init__(self, parent, title):
		super(FrameUI, self).__init__(parent, title = title, size =(300, 200))

		# function for in-frame components
		self.InitUI()

	def InitUI(self):
		# parent panel for radio box
		pnl = wx.Panel(self)


		# create static box
		self.sb = wx.StaticBox(pnl, 2, label ="Static Box",
							pos =(20, 20), size =(100, 100))

		# extra space for border
		print(self.sb.GetBorderdForSize())

		# set frame in centre
		self.Centre()
		# set size of frame
		self.SetSize((400, 250))
		# show output frame
		self.Show(True)



# wx App instance
ex = wx.App()
# Example instance
FrameUI(None, 'RadioButton and RadioBox')
ex.MainLoop()
