class Node:
	# make an empty node
	def __init__(self):
		self.cargo = None
		self.next = None

class linkedList:
	# initialize the list
	def __init__(self):
		self.head = None

	# add the content to the node then add the node to the linked list
	def newNode(self, text):
		newNode = Node()
		newNode.cargo = text
		newNode.next = self.head
		# add the node to the list
		self.head = newNode