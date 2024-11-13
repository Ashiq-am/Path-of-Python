def remove_last_node(self):

	if self.head is None:
		return

	current_node = self.head
	while(current_node.next.next):
		current_node = current_node.next

	current_node.next = None
