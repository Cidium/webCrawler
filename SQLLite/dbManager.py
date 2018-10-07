import sqlite3
import time
import datetime

class Link:
    def __init__(self,URL,VISITED_DATE, ADDED_DATE, REFERENCE_URL, REFERENCE_TIMES):
        self.URL = URL
        self.VISITED_DATE = VISITED_DATE
        self.ADDED_DATE = ADDED_DATE
        self.REFERENCE_URL = REFERENCE_URL
        self.REFERENCE_TIMES = REFERENCE_TIMES

class DBManager:
    def __init__(self,database):
        self.database = database

    def pushToDB(self,actual_url, parent_url):
        #conn = sqlite3.connect('webCrawler.db')
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        c.execute("INSERT OR IGNORE INTO webPages (URL, ADDED_DATE, REFERENCE_URL, REFERENCE_TIMES)  VALUES (?,?,?,1)",(actual_url,date,parent_url))
        conn.commit()
        c.close()
        conn.close()

    def getLink(self,url):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        c.execute("SELECT * FROM webPages WHERE URL=?",(url,))
        rows = c.fetchall()
        for row in rows:
            link = Link(row[0],row[1],row[2],row[3],row[4])
        conn.commit()
        c.close()
        conn.close()
        return link

    def getLinks(self, type):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()

        if type == "visited":
            c.execute("SELECT * FROM webPages WHERE VISITED_DATE IS NOT NULL")
        elif type == "not_visited":
            c.execute("SELECT * FROM webPages WHERE VISITED_DATE IS NULL")
        else:
            c.execute("SELECT * FROM webPages")

        rows = c.fetchall()
        links = []
        for row in rows:
            links.append(Link(row[0],row[1],row[2],row[3],row[4]))
        conn.commit()
        c.close()
        conn.close()
        return links
