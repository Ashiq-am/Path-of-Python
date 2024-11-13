class node:
	def __init__(self, ele):
		self.ele = ele
		self.left = None
		self.right = None


def preorder(self):
	if self:
		print(self.ele)
		preorder(self.left)
		preorder(self.right)


n = node('first')
n.left = node('second')
n.right = node('third')
preorder(n)
