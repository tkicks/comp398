"""scrapes states and territories from the web and puts them in a .csv file"""
from bs4 import BeautifulSoup
import urllib2
import csv

def main():
    """run scraper function"""
    scraper()

def scraper():
    """open page, scrape <li>s inside <ul>s to get the text and write to .csv"""

    # init BeautifulSoup on webpage
    wiki = "http://www.ilru.net/html/publications/directory/state_list.html"
    page = urllib2.urlopen(wiki)
    soup = BeautifulSoup(page)

    state = ""

    # find all <ul>
    table = soup.find("ul")
    # while writing to file keep it open
    with open('output.csv', 'w') as csv_file:

        # find all <li> and write the text inside to the file
        for row in table.findAll("li"):
            state = row.findAll(text=True)

            state_writer = csv.writer(csv_file, delimiter=" ")
            state_writer.writerow(state)

if __name__ == "__main__":
    main()
