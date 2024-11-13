def insertAtBegin(self, data):
	new_node = Node(data)
	if self.head is None:
		self.head = new_node
		return
	else:
		new_node.next = self.head
		self.head = new_node
