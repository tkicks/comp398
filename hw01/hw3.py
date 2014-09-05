import csv

class Node:
	def __init__(self, cargo, next):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)


def main():
	#make the lists
	newNode = []
	i = 0
	with open('output2.csv', 'r') as csvFile:
		for row in csvFile:
			# row = u'\xe4'.decode('utf-8')
			diseaseText = repr(row)
			newNode = Node(diseaseText, i)
			
			print newNode

			i += 1

			#newNode.next = i
			#print repr(row).strip("\n")

	print newNode[8]

if __name__=="__main__":
	main()