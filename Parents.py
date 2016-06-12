from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    return html

# test HTTPError

# Get price by IMG url
def getPrice(imgUrl):
    return bsObj.find("img", {"src":imgUrl}).parent.previous_sibling.get_text()

html = getHTML("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for img in bsObj.findAll("img", {"src":re.compile("\/img\/gifts\/img[0-9]+\.jpg")}):
    imgUrl = img['src']
    print(imgUrl, getPrice(imgUrl))

    
