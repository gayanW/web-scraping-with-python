from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

def getHTML(url):
    try:
        return urlopen("https://en.wikipedia.org" + url).read()
    except URLError:
        return None

def crawl(url):
    html = getHTML(url)
    if (html is None):
        print("Error getting HTML")
    else:
        bsObj = BeautifulSoup(html, "lxml")
        # print data
        print("-----", url)
        try:
            print(bsObj.h1.get_text())
            #print(bsObj.find(id="mw-content-text").p)
            print(bsObj.find(id="ca-edit").span.a['href'])
        except AttributeError as e:
            print(e)

        newUrl = findNewArticle(html)
        if (newUrl is not None):
            crawl(newUrl)
        else:
            print("No new articles found")



crawledUrls = set()
def findNewArticle(html):
    bsObj = BeautifulSoup(html, "lxml")
    for aTag in bsObj.findAll("a", href=re.compile("^/wiki/((?!:).)+$")):
        if (aTag['href'] not in crawledUrls):
            newUrl = aTag['href']
            crawledUrls.add(newUrl)
            return newUrl
    return None

# start crawling wikipedia
crawl("")
    
