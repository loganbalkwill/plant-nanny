#Created by Logan Balkwill
#Created on 8-30-2020

import mysql.connector
import settings

class Plant_Database:
    """Connector to plant database. Also provides writing functionality
    """
    
    def __init__(self):
        
        #Import database properties from settings.py
        self.host=settings.host
        self.username=settings.username
        self.password=settings.password
        self.db_name=settings.database_name

    def connect(self):
        #Attempt to make a connection to the database
        try:
            mysql.connector.connect(host=self.host,user=self.username,password=self.password,database=self.db_name)
            print("connection to database '%s' was successfull" % self.db_name)
        except:
            print("FAILED to connect to database '%s'" % self.db_name) 


if __name__=="__main__":
    print("Attempting DB Connection")
    x=Plant_Database()
    x.connect()
