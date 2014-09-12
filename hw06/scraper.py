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
    course_catalog = "https://weblprod1.wheatonma.edu/PROD/bzcrschd.P_OpenDoor"
    page = urllib2.urlopen(course_catalog)
    soup = BeautifulSoup(page)

    subjects = ""

    # find all <ul>
    table = soup.find("td")
    # while writing to file keep it open
    with open('subjectList.csv', 'w') as csv_file:

        # find all <li> and write the text inside to the file
        for row in table.findAll("submenulinktext2"):
            subjects = row.findAll(text=True)

            subject_writer = csv.writer(csv_file, delimiter=" ")
            subject_writer.writerow(subjects)

if __name__ == "__main__":
    main()
