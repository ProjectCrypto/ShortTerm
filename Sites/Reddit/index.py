#
#import re
#import pandas as pd
#import requests
#import json
#import time
#from bs4 import BeautifulSoup
#
#class Website(object):
#    """
#    Using the `__init__` to define columns and table name of SQL table to be stored.
#    Use the `execute` method to populate the created table.
#    
#    """
#    def __init__(self):
#        self.table    = 'NewsHistory'
#        self.Site     = 'TEXT'
#        self.Content  = 'TEXT'
#        self.Date     = 'FLOAT'
#        self.Title    = 'TEXT'
#        
#    def execute(self):
#        hdr = {'User-Agent': 'windows:r/politics.single.result:v1.0' + '(by /u/)'}
#        url = 'https://www.reddit.com/r/politics/.json'
#        req = requests.get(url, headers=hdr)
#        json_data = json.loads(req.text)
#        
#        
#        
#        
#        import praw
#        r = praw.Reddit(user_agent='Subreddit Parse Bot 2000',
#                        cache_timeout=0)
#        for comment in r.get_subreddit('Python') \
#                        .get_comments(limit=200):
#            print(comment.author.name,
#                  comment.body_html,
#                  comment.id,
#                  comment.submission.id)
#
#


