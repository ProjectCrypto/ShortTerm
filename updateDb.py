#!/Users/ericentrup/anaconda/bin/python2.7

import os
import time
import sqlite3
import pandas as pd
from glob import glob

from Utilities import dynamicImport

class Database(object):
    """
    Database is used to update data in database by executing webscraping modules.
    """
    def __init__(self):
        self.root     = os.path.dirname(os.path.abspath(__file__))
        self.database = os.path.join(self.root,'Sqlite3.db')
        
        if os.path.exists(self.database):
            os.remove(self.database)
            
            
    def main(self):
        websites = glob(os.path.join(self.root,'Sites/*'))
        for website in filter(os.path.isdir,websites):
            message = "...Searching {}"
            print message.format(os.path.basename(website))

            self.insert(dynamicImport(website))
        
        
    
    def insert(self,module):
        """
        Creates an instance of modules and uses attributes to populate fields in
        database. Then tries to create new table if one does not already exist. 
        Finally, will try to execute module to acquire data and then populate in
        database.
        """
        instance = module.Website()
        schema = instance.__dict__
        table  = schema.pop('table')
        attr   = lambda x: '{} {}'.format(x[0],x[1])
        fields = ','.join(map(attr,schema.items()))
        data   = instance.execute()
        
        with sqlite3.connect(self.database) as connection:
            query = """
                CREATE TABLE IF NOT EXISTS {} (
                    id INTEGER PRIMARY KEY, {}
                )
            """
            connection.execute(query.format(table,fields))
            
            data.to_sql(table,con = connection, if_exists='append', index=False)
            
    
    
    
if __name__ == "__main__":
    start = time.time()
    db = Database()
    db.main()
    end = time.time()
    print 'Finished in {0:.2f}s'.format(float(end) - start)