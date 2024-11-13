import wx

class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, parent = None, title ='TreeCtrl Demo')
		# tree control
		self.tree = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)

		# create imagelist
		il = wx.ImageList(16, 16)

		# add images to image list
		one = il.Add(wx.Image('plus.png', wx.BITMAP_TYPE_PNG).Scale(16, 16).ConvertToBitmap())
		two = il.Add(wx.Image('close.png').Scale(16, 16).ConvertToBitmap())

		# asign image list to tree
		self.tree.AssignImageList(il)

		# add a root node to tree
		self.root = self.tree.AddRoot('Root ', 0)

		# add item to self.root
		self.tree.AppendItem(self.root, "Item", 1)

		# expand tree
		self.tree.Expand(self.root)

		# show frame
		self.Show()


if __name__ == '__main__':
	app = wx.App(redirect = False)
	frame = MainFrame()
	app.MainLoop()
