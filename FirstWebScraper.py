from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    return html

def getTitle(html):
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

html = getHtml("http://www.pythonscraping.com/pages/page1.html")
title = getTitle(html)
if title == None:
    print("Title could not be found.")
else:
    print(title)
    
