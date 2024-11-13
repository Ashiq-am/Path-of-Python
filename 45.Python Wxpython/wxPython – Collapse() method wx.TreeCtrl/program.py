import wx


class MyTree(wx.TreeCtrl):

	def __init__(self, parent, id, pos, size, style):
		wx.TreeCtrl.__init__(self, parent, id, pos, size, style)


class TreePanel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		# create tree control
		self.tree = MyTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
															wx.TR_HAS_BUTTONS)

		self.btn = wx.Button(self, 1, "Collapse", (50, 60))

		# add root to self.tree
		self.root = self.tree.AddRoot('Root')
		# add item to self.root
		item = self.tree.AppendItem(self.root, 'Item')

		# bind event with self.btn
		self.btn.Bind(wx.EVT_BUTTON, self.onclick)

		self.tree.Expand(self.root)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.tree, 0, wx.EXPAND)
		self.SetSizer(sizer)

	def onclick(self, e):
		# collapse root
		self.tree.Collapse(self.root)

class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, parent = None, title ='TreeCtrl Demo')
		panel = TreePanel(self)
		self.Show()


if __name__ == '__main__':
	app = wx.App(redirect = False)
	frame = MainFrame()
	app.MainLoop()
