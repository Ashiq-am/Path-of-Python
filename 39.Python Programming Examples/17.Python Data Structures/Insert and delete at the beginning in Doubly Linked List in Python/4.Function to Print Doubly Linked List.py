def print_list(self):
	if self.head is None:
		print("List is empty")
		return
	curr = Node()
	curr = self.head
	while(curr != None):
		print(curr.data)
		curr = curr.next
	print()
