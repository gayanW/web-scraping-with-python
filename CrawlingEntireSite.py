from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

baseurl = "https://en.wikipedia.org"

def getHTML(url):
    try:
        return urlopen(baseurl + url)
    except URLError as e:
        print(e)
    return None

def getLinks(html):
    bsObj = BeautifulSoup(html, "lxml")
    links = bsObj.findAll("a", href=re.compile("^/wiki/((?!:).)+$"))
    return links

linkSet = set()
def crawlSite(url):
    html = getHTML(url)
    for link in getLinks(html):
        if link['href'] not in linkSet:
            newUrl = link['href']
            linkSet.add(newUrl)
            print(linkSet)
            crawlSite(newUrl)

crawlSite("/wiki/Main_Page");


    
