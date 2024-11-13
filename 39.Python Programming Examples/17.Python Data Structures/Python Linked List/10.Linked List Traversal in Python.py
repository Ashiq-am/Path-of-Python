def printLL(self):
	current_node = self.head
	while(current_node):
		print(current_node.data)
		current_node = current_node.next
