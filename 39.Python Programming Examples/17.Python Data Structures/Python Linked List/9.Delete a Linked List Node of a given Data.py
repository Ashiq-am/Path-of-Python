def remove_node(self, data):
	current_node = self.head

	# Check if the head node contains the specified data
	if current_node.data == data:
		self.remove_first_node()
		return

	while current_node is not None and current_node.next.data != data:
		current_node = current_node.next

	if current_node is None:
		return
	else:
		current_node.next = current_node.next.next
