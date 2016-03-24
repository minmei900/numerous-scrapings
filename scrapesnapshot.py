from bs4 import BeautifulSoup
import urllib2

ISE_API_URL = 'https://apps.butler.edu/snapshot/live/weekly.asp'
ISE_API_URL_TOP = 'https://apps.butler.edu/'
username = 'clmiller'
password = 'Too Many Julies!1'
   
# create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
password_mgr.add_password(None, ISE_API_URL_TOP, username, password)

handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

# use the opener to fetch a URL
opener.open(ISE_API_URL)

# Install the opener.
# Now all calls to urllib2.urlopen use our opener.
urllib2.install_opener(opener)

responsesplash = urllib2.urlopen(ISE_API_URL)
response = urllib2.urlopen(ISE_API_URL)
 
result = response.read()

soup = BeautifulSoup(result, "lxml")

print soup

#element1 = soup.find_all("count", limit=1)

#final = element1[0].string

#print final
