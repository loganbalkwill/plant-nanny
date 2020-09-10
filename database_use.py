#Created by Logan Balkwill
#Created on 8-30-2020

import mysql.connector
import settings


""" TODO
        -Logging database actions
        -
"""

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

    def write(self, table, write_info):
        #Write data to the database table
        
        #build SQL command string
        sql=build_SQL_insert(table)
        
        #insert into database
        try:
            cursor=self.connect.cursor()
            cursor.execute(sql, val)
            
            self.commit()
            
            print(cursor.rowcount, "record inserted")
        
        except:
            print("Failed to write to database")

        #mydb.commit()

        #print(mycursor.rowcount, "record inserted.")
        #print(sql)


def build_SQL_insert(table_name):
    #returns sql string of command
    
    if table_name=='soilsensor':
        return "INSERT INTO soilsensor (DateTime, plant_id, SoilTemp_DegC, SoilMoisture_val) VALUES (%s, %s, %s, %s)"
    else:
        return ''


if __name__=="__main__":
    print("Attempting DB Connection")
    x=Plant_Database()
    x.connect()
    x.write(table='soilsensor',write_info=['2020-08-31','testPlant',20,390])
