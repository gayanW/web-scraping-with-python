from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    return html

html = getHTML("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)
    
    
