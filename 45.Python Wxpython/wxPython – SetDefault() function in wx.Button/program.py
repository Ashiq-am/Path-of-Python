import wx


class MyDialog(wx.Dialog):
	def __init__(self, parent, title):
		super(MyDialog, self).__init__(parent, title = title, size =(250, 175))
		panel = wx.Panel(self)
		self.btn = wx.Button(panel, wx.ID_OK, label ="Default",
								size =(50, 20), pos =(75, 50))
		self.btn1 = wx.Button(panel, wx.ID_OK, label ="Not Default",
									size =(90, 20), pos =(75, 100))


class Mywin(wx.Frame):

	def __init__(self, parent, title):
		super(Mywin, self).__init__(parent, title = title, size =(250, 150))
		self.InitUI()

	def InitUI(self):
		panel = wx.Panel(self)
		btn = wx.Button(panel, label ="Click", pos =(75, 10))
		btn.Bind(wx.EVT_BUTTON, self.OnModal)
		# SET BUTTON AS DEFAULT
		btn.SetDefault()

		self.SetMinSize((600, 400))
		self.Centre()
		self.Show(True)

	def OnModal(self, event):
		a = MyDialog(self, "Dialog").ShowModal()

ex = wx.App()
Mywin(None, 'Window')
ex.MainLoop()
