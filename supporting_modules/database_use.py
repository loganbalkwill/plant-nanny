#Created by Logan Balkwill
#Created on 8-30-2020
import sys
sys.path.insert(0, '..')

import mysql.connector
import settings as s
import supporting_modules.logger as logger


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
        
        logger.log_info(log_level='p', message=str(cursor.rowcount) + (" record inserted to %s table" % table))
    
    except:
        #failed to write to the database; store info locally
        print("Failed to write to database")
        logger.log_locally(info=write_info, filename=table)
        

def build_SQL_insert(table_name):
    #returns sql string of command
    
    if table_name=='soilsensor_trans':
        return "INSERT INTO soilsensor_trans (DateTime, plant_id, SoilTemp_DegC, SoilMoisture_val) VALUES (%s, %s, %s, %s)"
    
    elif table_name=='gassensor_trans':
        return "INSERT INTO `gassensor_trans` (`record_id`, `DateTime`, `plant_id`, `eCO2_ppm`, `TVOC_ppb`) VALUES (NULL, %s, %s, %s, %s)"
    
    elif table_name=='lightsensor_trans':
        return "INSERT INTO `lightsensor_trans` (`record_id`, `DateTime`, `plant_id`, `colour_red`, `colour_green`, `colour_blue`, `colour_clear`) VALUES (NULL, %s, %s, %s, %s, %s, %s)"
    
    elif table_name=='airsensor_trans':
        return "INSERT INTO `airsensor_trans` (`record_id`, `DateTime`, `plant_id`, `AirTemp_DegC`, `AirHumidity_percent`, `AirGas_ohms`, `AirPressure_hpa`) VALUES (NULL, %s, %s, %s, %s, %s, %s)"
    
    elif table_name=='photo_trans':
        return "INSERT INTO `photo_trans` (`record_id`, `capture_datetime`, `plant_id`, `image_path`) VALUES (NULL, %s, %s, %s)"
    
    elif table_name=='log_trans':
        return "INSERT INTO `log_trans` (`record_id`, `datetime`, `log_type`, `log_message`) VALUES (NULL, %s, %s, %s)"
    
    else:
        return ''

def get_sensor_list(additional_sql):
    #returns list of active sensors
    
    #build SQL query string
    sql= "SELECT * FROM sensors"
    
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
    sql= "SELECT read_frequency_min FROM sensors"
    
    if len(additional_sql)>1:
        sql=sql + " WHERE " + additional_sql 
        
    #execute query
    mycursor=plant_db.cursor()
    mycursor.execute(sql)
    
    sensor_list=mycursor.fetchall()
        
    mycursor.close()
    
    return sensor_list

def build_plant_devices_list():
    #used to build the main list of plant devices and characteristics used in program
    
    #Output tuple as: PlantID, Plant Name, Device_ID, Device Name, Action_Frequency_Min
    
    #Build SQL string
    sql="SELECT DISTINCT D_PD.id_plant AS Plant_ID, D_P.name AS Plant_Name, D_PD.id_device AS Device_ID, D_D.model AS Device_Name, COALESCE(D_PD.action_freq_mins, D_D.default_action_freq_mins) AS Action_Frequency FROM def_plant_devices AS D_PD INNER JOIN def_plants AS D_P ON D_PD.id_plant=D_P.id INNER JOIN def_devices AS D_D ON D_PD.id_device=D_D.id WHERE D_P.active=1 AND D_D.supported=1 AND D_PD.active=1"
    
    #execute query
    mycursor=plant_db.cursor()
    mycursor.execute(sql)
    
    device_list=mycursor.fetchall()
        
    mycursor.close()
    
    return device_list

if __name__=="__main__":
    print("Attempting to write to DB")
    write_to_db(db=plant_db,table='soilsensor_trans',write_info=['2020-08-31','1',20,390])
