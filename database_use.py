#Created by Logan Balkwill
#Created on 8-30-2020

import mysql.connector
import settings

db_driver=''
db_server=''
db_name='plantnanny'


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
        
