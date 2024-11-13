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
		lblList = ['Radio One', 'Radio Two']

		# create radio box containing above list
		self.rbox = wx.RadioBox(pnl, label ='RadioBox', pos =(80, 10), choices = lblList,
								majorDimension = 1, style = wx.RA_SPECIFY_ROWS)

		# create a button in the frame
		self.btn = wx.Button(pnl, 1, "Hide RadioBox", pos =(125, 100));
		# create a button in the frame
		self.btn1 = wx.Button(pnl, 2, "Show RadioBox", pos =(125, 150));

		# bind a function with button btn
		self.btn.Bind(wx.EVT_BUTTON, self.onclick)
		# bind a function with button btn1
		self.btn1.Bind(wx.EVT_BUTTON, self.onclick1)

		# set frame in centre
		self.Centre()

		# set size of frame
		self.SetSize((400, 250))

		# show output frame
		self.Show(True)

	def onclick(self, e):
		# hide radio box from the frame
		self.rbox.Show(False)

	def onclick1(self, e):
		# shows radio box
		self.rbox.Show()


# wx App instance
ex = wx.App()
# Example instance
FrameUI(None, 'RadioButton and RadioBox')
ex.MainLoop()
