from bs4 import BeautifulSoup
import urllib2
import json

count=0
page = urllib2.urlopen("https://adm.butler.edu/manage/query/process?id=f6949a17-c1ab-4234-85d2-c8d6f821b67f&h=902b7855-91af-fc3d-aafa-9cf4d7f00870&output=json")


result = page.read()

#soup = BeautifulSoup(result, "lxml")
jason = json.loads(result)

#print soup.prettify()
#print json.dumps(jason, sort_keys=True, indent=4, separators=(',', ': '))
#print jason

print jason["row"][0]["Apps"]


