import csv

class Node:
	def __init__(self):
		self.cargo = None
		self.next = None

	# def __str__(self):
	# 	return str(self.cargo)


def main():
	#make the lists
	with open('output2.csv', 'r') as csvFile:
		currentNode = Node()
		nextNode = Node()
		for row in csvFile:
			# row = u'\xe4'.decode('utf-8')
			diseaseText = repr(row.strip())

			currentNode.cargo = diseaseText
			currentNode.next = nextNode
			#newNode = Node(diseaseText)
			
			print currentNode.cargo
			#print currentNode.next


			#newNode.next = i
			#print repr(row).strip("\n")

	#print newNode[8]

	while currentNode.next != None:
		#currentNode = 
		print currentNode.cargo
		currentNode = currentNode.next

if __name__=="__main__":
	main()