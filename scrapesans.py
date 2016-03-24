from bs4 import BeautifulSoup
import urllib

page = urllib.urlopen("https://isc.sans.edu/api/asnum/10/26026")

result = page.read()

soup = BeautifulSoup(result, "lxml")

#print soup

element1 = soup.find_all("reports", limit=1)

final = element1[0].string

print final
