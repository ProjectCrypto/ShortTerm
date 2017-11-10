import re
import pandas as pd

import requests

class Website(object):
    """
    Uniquely gather data from website and send back to PriceHistory
    """
    def __init__(self):
        self.table = 'PriceHistory'
        self.Date  = 'FLOAT'
        self.Price = 'FLOAT'
        self.Type  = 'TEXT'
        self.Unit  = 'TEXT'
        self.Site  = 'TEXT'
        
        
        
    def execute(self):
        url = "http://finance.yahoo.com/quote/{0}?p={0}"
        response = requests.get(url.format('aapl'))
        #import pdb;pdb.set_trace()
        return pd.DataFrame()