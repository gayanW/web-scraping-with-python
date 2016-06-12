from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    return html

html = getHTML("http://www.pythonscraping.com/pages/page3.html")

# select all the rows in the table, without select‐ing the title row itself
if (html == None):
    print("HTTPError")
else:
    bsObj = BeautifulSoup(html, "lxml")
    for row in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
        print(row)
    

        
