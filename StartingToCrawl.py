from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import random
import datetime

# program to traverse over wikipedia articles

def getHTML(url):
    try:
        html = urlopen(url)
        return html
    except URLError as e:
        print(e)
    return None

def getLinks(href):
    html = getHTML("https://en.wikipedia.org" + href)
    if html is not None:
        bsObj = BeautifulSoup(html, "lxml")
        return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(\/wiki\/)((?!:).)*$"))
    else:
        return None

links = getLinks("/wiki/Eric_Idle")
random.seed(datetime.datetime.now)

# chooses a random article link from the returned list, 
# and calls getLinks again, until we stop the program or 
# until there are no article links found on the new page.
while (links is not None) and (len(links) > 0):
    randUrl = links[random.randint(0, len(links) - 1)]['href']
    links = getLinks(randUrl)
    print(randUrl)
    
