"""scrapes states and territories from the web and puts them in a .csv file"""
from bs4 import BeautifulSoup
import urllib2
import csv

def main():
    scraper()

def scraper():
    """open page, scrapes li's inside ul's to get the text and writes to .csv"""

    wiki = "http://www.ilru.net/html/publications/directory/state_list.html"
    page = urllib2.urlopen(wiki)
    soup = BeautifulSoup(page)

    state = ""

    table = soup.find("ul")
    with open('output.csv', 'w') as csv_file:

        for row in table.findAll("li"):
            state = row.findAll(text=True)

            state_writer = csv.writer(csv_file, delimiter=" ")
            state_writer.writerow(state)

if __name__ == "__main__":
    main()
