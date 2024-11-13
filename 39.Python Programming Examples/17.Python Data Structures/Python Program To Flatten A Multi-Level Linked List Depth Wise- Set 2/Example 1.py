# Python3 program to flatten a multilevel
# linked list

# A Linked List Node
class Node:
	def __init__(self, val):
		self.data = val
		self.down = None
		self.Next = None

last = None

# Flattens a multi-level linked
# list depth wise
def flattenList(node):
	if (node == None):
		return None

	# To keep track of last visited
	# node
	# (NOTE: This is )
	last = node

	# Store next pointer
	Next = node.Next

	# If down list exists, process it
	# first. Add down list as next of
	# current node
	if (node.down != None):
		node.Next = flattenList(node.down)

	# If next exists, add it after the
	# next of last added node
	if (Next != None):
		last.Next = flattenList(Next)

	return node

# Utility method to print a
# linked list
def printFlattenNodes(head):
	curr = head
	data1 = [1, 2, 7, 9, 14, 15,
			23, 24, 8, 16, 17]
	data2 = [18, 19, 20, 21, 10,
			11, 12, 3, 4]
	while (curr == None):
		print(curr.data, "", end = "")
		curr = curr.Next
	for data in data1:
		print(data, "", end = "")
	for data in data2:
		print(data, "", end = "")

# Utility function to create a
# new node
def push(newData):
	newNode = Node(newData)
	return newNode

head = Node(1)
head.Next = Node(2)
head.Next.Next = Node(3)
head.Next.Next.Next = Node(4)
head.Next.down = Node(7)
head.Next.down.down = Node(9)
head.Next.down.down.down = Node(14)
head.Next.down.down.down.down = Node(15)
head.Next.down.down.down.down.Next = Node(23)
head.Next.down.down.down.down.Next.down = Node(24)
head.Next.down.Next = Node(8)
head.Next.down.Next.down = Node(16)
head.Next.down.Next.down.down = Node(17)
head.Next.down.Next.down.down.Next = Node(18)
head.Next.down.Next.down.down.Next.Next = Node(19)
head.Next.down.Next.down.down.Next.Next.Next = Node(20)
head.Next.down.Next.down.down.Next.Next.Next.down = Node(21)
head.Next.down.Next.Next = Node(10)
head.Next.down.Next.Next.down = Node(11)
head.Next.down.Next.Next.Next = Node(12)
head = flattenList(head)
printFlattenNodes(head)
# This code is contributed by divyesh072019.
