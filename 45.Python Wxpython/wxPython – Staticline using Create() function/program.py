import wx


class FrameUI(wx.Frame):

	def __init__(self, parent, title):
		super(FrameUI, self).__init__(parent, title = title, size =(300, 200))

		# function for in-frame components
		self.InitUI()

	def InitUI(self):
		# parent panel for radio box
		pnl = wx.Panel(self)

		# list of choices
		hlist = ['Item One', 'Item Two']
		vlist =['Item One', 'Item Two']

		# initialize a static line
		self.sl = wx.StaticLine()

		# add attributes using Create() function
		self.sl.Create(pnl, 2, pos =(50, 0), size = (1, 250),
									style = wx.LI_VERTICAL)

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
