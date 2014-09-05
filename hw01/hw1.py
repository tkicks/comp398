from bs4 import BeautifulSoup
import urllib2
import csv
#import urllib.request
#import unicode
 
wiki = "http://en.wikipedia.org/wiki/List_of_infectious_diseases"
# header = {'User-Agent': 'Mozilla/5.0'}
# req = urllib.request.Request(wiki, headers=header)
#page = urllib.request.urlopen(wiki)
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)
 
disease = ""
source = ""
diseaseList = []
 
table = soup.find("table")
f = open('output.csv', 'w')
 
for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 2:
        disease = cells[0].findAll(text=True)
        source = cells[1].findAll(text=True)
        diseaseList.append(disease + "," + source)

        # unicode.join(u'\n', map(unicode,disease))
        # unicode.join(u'\n', map(unicode,source))
    #f.write(disease + "," + source)

f.write(diseaseList)
 
f.close()