import wx

class Tree(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		# create Tree Control in frame
		self.tree = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition,
												wx.DefaultSize,
												wx.TR_HAS_BUTTONS)

		# Create root for Tree Control
		self.root = self.tree.AddRoot('Root')

		# Add item to root
		item = self.tree.AppendItem(self.root, 'Item')

		# Clear focused item
		self.tree.ClearFocusedItem()

		# expand tree
		self.tree.Expand(self.root)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.tree, 0, wx.EXPAND)
		self.SetSizer(sizer)

# main root frame for tree control
class rootframe(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title ='TreeCtrl Demo')
		panel = Tree(self)
		self.Show()


if __name__ == '__main__':
	app = wx.App(redirect = False)
	frame = rootframe()
	app.MainLoop()
