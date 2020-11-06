#Created by Logan Balkwill
#Created on 8-30-2020
import sys
from importlib import reload
sys.path.insert(0, '..')

import mysql.connector
import settings as s
import dictionaries

#The below import statement is used in the log_information function
import supporting_modules.logger as logger
reload(logger)

""" TODO
        -Logging database actions
"""

def log_information(severity, msg):
    #import supporting_modules.logger as logger
    logger.log_info(log_level=severity, message=msg)
    
def log_locally(i, f):
    #import supporting_modules.logger as logger
    logger.log_locally(info=i,filename=f)
    

#Import SQL dictionaries:
sql_insert=dictionaries.sql_insert.copy()
sql_select=dictionaries.sql_select.copy()

#Establish connection to database
try:
    plant_db=mysql.connector.connect(host=s.host,
                                     user=s.username,
                                     password=s.password,
                                     database=s.database_name)
    
    log_information(severity='p',
                    msg=("connection to database '%s' was successfull" % s.database_name))
    
except:
    log_information(severity='p',
                    msg=("FAILED to connect to database '%s'" % s.database_name)) 


def write_to_db(table, write_info,db=plant_db, log_local=True):
    #Write data to the database table
    
    #build SQL command string
    sql=build_SQL_insert(table)
    
    #insert into database
    try:
        cursor=db.cursor()
        cursor.execute(sql, write_info)
        
        db.commit()
        
        log_information(severity='p', msg=str(cursor.rowcount) + (" record inserted to %s table" % table))
    
    except:
        #failed to write to the database; store info locally
        log_information(severity='p', msg="Failed to write to database")
        if log_local==True:
            log_locally(i=write_info, f=table)
        else: raise Exception("Information not logged!!!")
        

def build_SQL_insert(table_name):
    #returns sql string of command
    
    if table_name in sql_insert:
        return sql_insert[table_name]
    else:
        return ''


def get_sensor_list(additional_sql):
    #returns list of active sensors
    
    #build SQL query string
    sql= sql_select['sensors']
    
    if len(additional_sql)>1:
        sql=sql + " WHERE " + additional_sql 
        
    #execute query
    mycursor=plant_db.cursor()
    mycursor.execute(sql)
    
    sensor_list=mycursor.fetchall()
    mycursor.close()
    
    return sensor_list

def get_sensor_frequencies(additional_sql):
    #returns list of sensor read frequencies
    
    #build SQL query string
    sql= sql_select['sensor_freq']
    
    if len(additional_sql)>1:
        sql=sql + " WHERE " + additional_sql 
        
    #execute query
    mycursor=plant_db.cursor()
    mycursor.execute(sql)
    
    sensor_list=mycursor.fetchall()
        
    mycursor.close()
    
    return sensor_list

def build_plant_devices_list():
    #Used to build the main list of plant devices and characteristics used in program
    #Output tuple as: PlantID, Plant Name, Device_ID, Device Name, Action_Frequency_Min
    
    #Get SQL string
    sql=sql_select['plant_devices'] 

    #execute query
    mycursor=plant_db.cursor()
    mycursor.execute(sql)
    
    device_list=mycursor.fetchall()
        
    mycursor.close()
    
    return device_list

def retrieve_data(sql_query, db=plant_db):
    #generic function to run sql_query and return result object
    
    #Validate the query string
    if (sql_query.find('SELECT')==-1) and (sql_query.find('select')==-1):
        #INVALID!! the provided string may be a 'UPDATE','DELETE', or other style string
        raise Exception('Error retrieving info from database... SQL string does not contain a SELECT statement!!')
    
    try:
        mycursor=db.cursor()
        mycursor.execute(sql_query)
        query_results=mycursor.fetchall()
        mycursor.close() 
    except:
        raise Exception('Unable to run SQL query. Verify the SQL string and database connection information')
   
    return query_results

if __name__=="__main__":
    log_information(severity='p', msg="Attempting to write to DB")
    write_to_db(db=plant_db,table='soilsensor_trans',write_info=['2020-08-31','1',20,390])
