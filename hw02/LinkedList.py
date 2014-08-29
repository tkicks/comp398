"""classes for driver.py
   pylint R error for both classes - wants methods"""

class Node(object):
    """make an empty node"""
    def __init__(self):
        self.cargo = None
        self.next = None

class LinkedList(object):
    """initialize the list"""
    def __init__(self):
        self.head = None

    def new_node(self, text):
        """add the content to the node then add the node to the linked list"""
        new_node = Node()
        new_node.cargo = text
        new_node.next = self.head
        # add the node to the list
        self.head = new_node
