#Created by Logan Balkwill
#Created on 8-30-2020

import mysql.connector
import settings as s


""" TODO
        -Logging database actions
"""

try:
    plant_db=mysql.connector.connect(host=s.host,
                                     user=s.username,
                                     password=s.password,
                                     database=s.database_name)
    
    print("connection to database '%s' was successfull" % s.database_name)
    
except:
    print("FAILED to connect to database '%s'" % s.database_name) 


def write_to_db(table, write_info,db=plant_db):
    #Write data to the database table
    
    #build SQL command string
    sql=build_SQL_insert(table)
    
    #insert into database
    try:
        cursor=db.cursor()
        cursor.execute(sql, write_info)
        
        db.commit()
        
        print(cursor.rowcount, "record inserted to %s table" % table)
    
    except:
        print("Failed to write to database")



def build_SQL_insert(table_name):
    #returns sql string of command
    
    if table_name=='soilsensor_trans':
        return "INSERT INTO soilsensor_trans (DateTime, plant_id, SoilTemp_DegC, SoilMoisture_val) VALUES (%s, %s, %s, %s)"
    else:
        return ''

def get_sensor_list(additional_filters):
    #returns list of active sensors
    
    #build SQL query string
    sql= "SELECT * FROM sensors WHERE active=1"
    
    if len(additional_filters)>1:
        sql=sql + " AND " + additional_filters 
        
    #execute query
    mycursor=plant_db.cursor()
    mycursor.execute(sql)
    
    sensor_list=mycursor.fetchall()
    return sensor_list
    
if __name__=="__main__":
    print("Attempting to write to DB")
    write_to_db(db=plant_db,table='soilsensor_trans',write_info=['2020-08-31','testPlant',20,390])
