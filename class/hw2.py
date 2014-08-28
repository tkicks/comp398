from bs4 import BeautifulSoup
import urllib2
import csv

class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)
 
def main():
	wiki = "http://www.ilru.net/html/publications/directory/state_list.html"
	page = urllib2.urlopen(wiki)
	soup = BeautifulSoup(page)
	 
	disease = ""
	 
	table = soup.find("ul")
	with open('output.csv', 'w') as csvFile:

		for row in table.findAll("li"):
		    state = row.findAll(text=True)

		    diseaseWriter = csv.writer(csvFile, delimiter = " ")
		    diseaseWriter.writerow(state)
	makeLists()

def makeLists():
	#make the lists
	with open('output.csv', 'r') as csvFile:
		for row in csvFile:
			print repr(row)


if __name__=="__main__":
	main()