# class to define node for the Augmented BST
class AugmentedBSTNode:
	def __init__(self, value):
		self.value = value
		self.size = 1
		self.left = None
		self.right = None

# class to define the augmented BST with the operations
class AugmentedBST:
	def __init__(self):
		self.root = None

	# Method to insert a value in the BST
	def insert(self, value):
		self.root = self._insert(self.root, value)

	# Helper Method to insert a node in the Augmented BST
	def _insert(self, node, value):
		if not node:
			return AugmentedBSTNode(value)
		node.size += 1
		if value <= node.value:
			node.left = self._insert(node.left, value)
		else:
			node.right = self._insert(node.right, value)
		return node

	# Method to query in the BST
	def query(self, k):
		return self._query(self.root, k)

	# Helper Method to query in the BST
	def _query(self, node, k):
		if not node:
			return 0
		if node.value <= k:
			return (node.left.size if node.left else 0) + 1 + self._query(node.right, k)
		else:
			return self._query(node.left, k)


# Example usage:
augmented_ds = AugmentedBST()
augmented_ds.insert(5)
augmented_ds.insert(2)
augmented_ds.insert(8)
augmented_ds.insert(1)

result = augmented_ds.query(6)
print(result)
