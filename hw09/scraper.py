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
	course_catalog = "file:///home/tkicks/Documents/comp/398/hw09/fall2014.html"
	page = urllib2.urlopen(course_catalog)
	soup = BeautifulSoup(page)
	courses = ""
	# find all <ul>
	table = soup.find("table")
	# while writing to file keep it open
	with open('subjectList.txt', 'w') as csv_file:
		# find all <li> and write the text inside to the file
		for row in table.findAll("tr"):
			courses = row.findAll(text=True)
			course_writer = csv.writer(csv_file)
			course_writer.writerow(courses)


if __name__ == "__main__":
	main()