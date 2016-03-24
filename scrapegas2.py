from bs4 import BeautifulSoup
import urllib

page = urllib.urlopen("http://www.gasbuddy.com/station/750")

result = page.read()

soup = BeautifulSoup(result, "lxml")

element1 = soup.find_all("div", class_="price-display credit-price", limit=1)

final = element1[0].string

print final
