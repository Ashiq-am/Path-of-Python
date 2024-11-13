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

		# create radio box with items in horizontal orientation
		self.rbox = wx.RadioBox(pnl, label ='RadioBox', pos =(10, 10), choices = hlist,
								majorDimension = 0, style = wx.RA_SPECIFY_ROWS)

		# create radio box with items in vertical orientation
		self.rbox = wx.RadioBox(pnl, label ='RadioBox', pos =(240, 10), choices = vlist,
								majorDimension = 0, style = wx.RA_SPECIFY_COLS)
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
