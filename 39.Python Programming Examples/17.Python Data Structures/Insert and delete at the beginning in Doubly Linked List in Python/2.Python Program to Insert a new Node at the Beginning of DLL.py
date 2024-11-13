def insert_at_begin(self, data):
	new_node = Node(data)
	if self.head is None:
		self.head = new_node
	else:
		self.head.prev = new_node
		new_node.next = self.head
		self.head = new_node
