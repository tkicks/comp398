#!/usr/bin/env python
import csv
import LinkedList


def main():
	# make the nodes from the .csv file and put them into a linked list
	with open('data.txt', 'r') as csvFile:
		lists = LinkedList.linkedList()
		for row in csvFile:
			diseaseText = repr(row.strip())
			lists.newNode(diseaseText)

	# print the list to the console (currently prints in reverse order of addition to the list)
	currentNode = lists.head
	while currentNode.next != None:
		print currentNode.cargo
		currentNode = currentNode.next

	# print only the diseases beginning with user inputted letter
	hasDiseases = False
	print " "
	searchFor = raw_input("Enter a letter to narrow search (A-G): ")
	print " "
	currentNode = lists.head
	while currentNode.next != None:
		if currentNode.cargo[1] == searchFor:
			print currentNode.cargo
			hasDiseases = True
		currentNode = currentNode.next
	if !hasDiseases:
		print "List not extensive enough, no diseases found."
	print " "

if __name__ == "__main__":
	main()