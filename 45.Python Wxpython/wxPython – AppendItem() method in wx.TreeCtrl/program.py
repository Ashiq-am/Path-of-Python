import wx

class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, parent = None, title ='TreeCtrl Demo')
		# tree control
		self.tree = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)

		# add a root node to tree
		self.root = self.tree.AddRoot('Root ')

		# add item to self.root
		self.tree.AppendItem(self.root, "Item")

		# expand tree
		self.tree.Expand(self.root)

		# show frame
		self.Show()


if __name__ == '__main__':
	app = wx.App(redirect = False)
	frame = MainFrame()
	app.MainLoop()
