def remove_first_node(self):
    if (self.head == None):
        return

    self.head = self.head.next
