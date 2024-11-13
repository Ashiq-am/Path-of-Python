# Deletes alternate nodes of a list
# starting with head
def deleteAlt(head):
	if (head == None):
		return

	node = head.next

	if (node == None):
		return

	# Change the next link of head
	head.next = node.next

	# Free memory allocated for node
	free(node)

	# Recursively call for the new
	# next of head
	deleteAlt(head.next)
# This code is contributed by Srathore
