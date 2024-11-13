import wx

class TreePanel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		self.tree = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, (100, 50),
						wx.TR_HAS_BUTTONS)
		# create tree root
		self.root = self.tree.AddRoot('root')
		self.tree.SetPyData(self.root, ('key', 'value'))

		# add items to root
		item = self.tree.AppendItem(self.root, "Item")
		item2 = self.tree.AppendItem(self.root, "Item")
		item3 = self.tree.AppendItem(self.root, "Item")
		item4 = self.tree.AppendItem(self.root, "Item")
		focusitem = self.tree.AppendItem(self.root, "Focus Item")

		# expand root
		self.tree.Expand(self.root)

		self.tree.EnsureVisible(focusitem)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.tree, 0, wx.EXPAND)
		self.SetSizer(sizer)

	def onclick(self, e):
		# Delete si2 from the tree
		self.tree.Delete(self.si2)


class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, parent = None, title ='TreeCtrl Demo')
		panel = TreePanel(self)
		self.Show()


if __name__ == '__main__':
	app = wx.App(redirect = False)
	frame = MainFrame()
	app.MainLoop()
