
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

class Website(object):
    """
    Using the `__init__` to define columns and table name of SQL table to be stored.
    Use the `execute` method to populate the created table.
    
    """
    def __init__(self):
        self.table    = 'NewsHistory'
        self.Site     = 'TEXT'
        self.Content  = 'TEXT'
        self.Date     = 'FLOAT'
        self.Title    = 'TEXT'
        
    def execute(self):
        links = []
        data  = []
        url   = 'https://www.cryptocoinsnews.com/'

        content = self.openLink(url)
        
        if content:
            soup = BeautifulSoup(content,'lxml')
            for link in soup.find_all('a',class_='grid-thumb-image'):
                title = link['title']
                href  = link['href']
                links.append((title,href))

            parsed = self.parseText(links)
            
            if parsed:
                data = parsed

        return pd.DataFrame(data, columns = ['Title','Site','Content'])


    def openLink(self,link):
        request = requests.get(link)
        if request.status_code == 200:
            content = request.text
        else:
            content = False
            
        return content
            
    def parseText(self,items):
        cleaned = []
        for item in items:
            baseurl = filter(None,item[1].split('/'))[1]
            content = self.openLink(item[1])
            if content:
                soup = BeautifulSoup(content,'lxml')
                for dom in soup(['style', 'script', '[document]', 'head', 'title']):
                    dom.extract()
                cleaned.append((item[0],baseurl,soup.get_text()))
                
        return cleaned
                