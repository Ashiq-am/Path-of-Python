# A complete working Python program to
# find the length of a Linked List
# iteratively

# Node class
class Node:

	# Function to initialize the node object
	def __init__(self, data):

		# Assign data
		self.data = data

		# Initialize next as null
		self.next = None

# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function is in LinkedList class.
	# It inserts a new node at the beginning
	# of Linked List.
	def push(self, new_data):

		# 1 & 2: Allocate the Node &
		#	 Put in the data
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to the new Node
		self.head = new_node

	# This function counts number of nodes in
	# Linked List iteratively, given 'node'
	# as starting node.
	def getCount(self):

		# Initialise temp
		temp = self.head
		count = 0 # Initialise count

		# Loop while end of linked list is
		# not reached
		while (temp):
			count += 1
			temp = temp.next
		return count

# Code execution starts here
if __name__=='__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(3)
	llist.push(1)
	llist.push(2)
	llist.push(1)
	print ("Count of nodes is :",llist.getCount())
