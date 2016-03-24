from bs4 import BeautifulSoup
import urllib

count=0
page = urllib.urlopen("http://www.skysports.com/football/competitions/premier-league/table")

result = page.read()

soup = BeautifulSoup(result, "lxml")

#print soup.prettify()

element1 = soup.find_all("td", class_="standing-table__cell--name")

for element in element1:

    count+=1
#    print element
#    print count
    if element.find_all(string="Arsenal"):
        print count

