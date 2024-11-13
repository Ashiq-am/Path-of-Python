def delete_at_begin(self):
	if self.head is None:
		print("List is empty")
	elif self.head.next is None:
		self.head = None
	else:
		self.head = self.head.next
		self.head.prev = None
