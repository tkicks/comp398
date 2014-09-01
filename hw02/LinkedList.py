"""classes for driver.py"""

#pylint: disable=too-few-public-methods
# above disables R0903 -- too few public methods in Node class

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
        # remove the "s and 's -----
        text = text.replace("'", "")
        text = text.replace('"', "")
        # --------------------------
        new_node.cargo = text
        new_node.next = self.head
        # add the node to the list
        self.head = new_node

    def print_list(self):
        """print the list to the console
        (currently prints in reverse alphabetical order)"""
        current_node = self.head
        while current_node.next != None:
            print current_node.cargo
            current_node = current_node.next
