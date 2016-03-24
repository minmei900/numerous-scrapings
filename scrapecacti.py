from bs4 import BeautifulSoup
import urllib

page = urllib.urlopen("http://caroline.butler.edu/cacti")

result = page.read()

soup = BeautifulSoup(result, "lxml")


print soup.prettify()








#element1 = soup.find_all("div", class_="price-display credit-price", limit=1)

#final = element1[0].string

#print final
