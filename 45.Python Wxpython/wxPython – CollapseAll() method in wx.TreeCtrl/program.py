import wx


class MyTree(wx.TreeCtrl):

	def __init__(self, parent, id, pos, size, style):
		wx.TreeCtrl.__init__(self, parent, id, pos, size, style)


class TreePanel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		# create Tree Control
		self.tree = MyTree(self, wx.ID_ANY, wx.DefaultPosition, (100, 70),
						wx.TR_HAS_BUTTONS)

		# Add root to Tree Control
		self.root = self.tree.AddRoot('Something goes here')

		# Add item to root
		itm = self.tree.AppendItem(self.root, 'Operating Systems')

		# Add item to 'itm'
		self.tree.AppendItem(itm, "Sub Item")

		# Expand whole tree
		self.tree.Expand(self.root)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.tree, 0, wx.EXPAND)
		self.SetSizer(sizer)

		# Add button in frame
		self.btn = wx.Button(self, 1, "Collapse", (10, 100))
		# Bind event function with button
		self.btn.Bind(wx.EVT_BUTTON, self.onclick)

	def onclick(self, e):
		# Collapse root of tree
		self.tree.CollapseAll()


class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, parent=None, title='TreeCtrl Demo')
		panel = TreePanel(self)
		self.Show()


if __name__ == '__main__':
	app = wx.App(redirect=False)
	frame = MainFrame()
	app.MainLoop()
