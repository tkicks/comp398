from bs4 import BeautifulSoup
import urllib2
import csv
#import urllib.request

class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)
 
def main():
	wiki = "http://en.wikipedia.org/wiki/List_of_infectious_diseases"
	# header = {'User-Agent': 'Mozilla/5.0'}
	# req = urllib.request.Request(wiki, headers=header)
	#page = urllib.request.urlopen(wiki)
	page = urllib2.urlopen(wiki)
	soup = BeautifulSoup(page)
	 
	disease = ""
	#source = ""
	 
	table = soup.find("table")
	with open('output.csv', 'w') as csvFile:

		for row in table.findAll("tr"):
		    cells = row.findAll("td")
		    if len(cells) == 2:
		        disease = cells[0].findAll(text=True)
		        #source = cells[1].findAll(text=True)

		        # if disease == u'\xe4':
		        # 	disease = u'\xe4'.encode("ascii", "ignore")
		        ###disease = u'\xe4'.encode('utf-8')
		        #unicode.join(u'\xe4', map(unicode,disease))
		        #unicode.join(u'\n', map(unicode,source))
		    #f.write(disease + "," + source)
		    str(disease).encode('utf-8').replace(u'\xe4', '*')
		    diseaseWriter = csv.writer(csvFile, delimiter = " ")
		    diseaseWriter.writerow(disease)
		    #diseaseWriter.writerow(source)
	 
	#csvfile.close()
	makeLists()

def makeLists():
	#make the lists
	with open('output.csv', 'r') as csvFile:
		for row in csvFile:
			row = u'\xe4'.decode('utf-8')
			#newNode = row.readline()
			print repr(row)


if __name__=="__main__":
	main()