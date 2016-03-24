from bs4 import BeautifulSoup
import urllib2
import sys

ISE_API_URL = 'https://prime.butler.edu/webacs/api/v1/data/ClientDetails'
ISE_API_URL_TOP = 'https://prime.butler.edu/'
username = 'apiaccess'
password = 'dr5tgy7uji9olP'
   
try: 	
    if sys.argv[1] != "none" :

        ISE_API_URL = 'https://prime.butler.edu/webacs/api/v1/data/ClientDetails?.full=true&userName="' + sys.argv[1] + '"'
    
except IndexError:

    print

print ISE_API_URL

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

response = urllib2.urlopen(ISE_API_URL)
 
result = response.read()

soup = BeautifulSoup(result, "lxml")

#element1 = soup.find_all("count", limit=1)

#final = element1[0].string

print soup
