from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime

# program to traverse over wikipedia articles

def getHTML(url):
    try:
        html = urlopen(url)
        return html
    except HTTPError as e:
        return None

def getLinks(href):
    bsObj = BeautifulSoup(getHTML("https://en.wikipedia.org" + href), "lxml")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(\/wiki\/)((?!:).)*$"))

links = getLinks("/wiki/Eric_Idle")
random.seed(datetime.datetime.now)

# chooses a random article link from the returned list, 
# and calls getLinks again, until we stop the program or 
# until there are no article links found on the new page.
while len(links) > 0:
    randUrl = links[random.randint(0, len(links) - 1)]['href']
    links = getLinks(randUrl)
    print(randUrl)
        
    
