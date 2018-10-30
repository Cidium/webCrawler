from dbManager import Link
from dbManager import DBManager
import urllib.request, re

database = DBManager("webCrawler.db")
visited = []

def nextlink():
    global visited
    links = database.getLinks("not_visited")
    most_referenced = 0
    most_referenced_url = ''
    for link in links:
        if link.URL not in visited:
            if link.REFERENCE_TIMES > most_referenced:
                most_referenced = link.REFERENCE_TIMES
                most_referenced_url = link.URL
    return (most_referenced_url)

url = ("https://www.github.com")
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
texto = str(html)
linko = url
c = True

while c == True:
    req = urllib.request.Request(linko, headers=hdr)
    html = urllib.request.urlopen(req).read()
    texto = str(html)
    enlaces = re.findall('href="(' + linko + '.*?)"', texto)
    for enlace in enlaces:
        database.pushToDB(enlace,linko)
    visited.append(linko)
    linko = nextlink()
    if linko == '':
        c = False
    print("going to next link: " + linko)

    
    
    
#link = database.getLink("https://www.animeyt.tv/animes")
#print(link.URL)
#print(link.VISITED_DATE)
#print(link.ADDED_DATE)
#print(link.REFERENCE_URL)
#print(link.REFERENCE_TIMES)

    


