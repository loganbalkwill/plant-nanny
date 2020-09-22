# import math
# import time
# import os
import sys
# import subprocess
# from datetime import datetime
# from picamera import PiCamera
#
#sys.path.append("..\<parent_folder>")
sys.path.insert(0, '..')

import settings
import database_use
import sensors




def get_photos_path(plant_id, plant_name):   
    #Build the string of file name + location
    path= settings.image_directory
    sub_path=str(plant_id) + "|" + str(plant_name)
    now=datetime.now()
    filename=str(now.strftime("%m-%d-%Y %H:%M:%S"))
    filetype=settings.image_filetype
    
    fullpath=path+ sub_path + '/' + filename + filetype
    
    #Make directory if doesnt already exist
    if os.path.exists(path + sub_path)==False:
        os.mkdir(path + sub_path + '/')
    
    return fullpath
    
def perform_action(action):
    #called by main loop when specified frequency has elapsed
    
    #input supplied as list in form:
    #PlantID, Plant Name, Device_ID, Device Name, Action_Frequency_Min
    
    plant_id, plant_name, device_id, device_name, action_freq, =action
    
    #decide what action to perform
    if device_name=='STEMMA Soil Sensor':
        #retrieve values and insert record into database
        soil_temp=sensors.get_soil_temp()
        soil_moisture=sensors.get_soil_moisture()
        
        database_use.write_to_db(table='soilsensor_trans',
                                 write_info=[datetime.now(),
                                             plant_id,
                                             soil_temp,
                                             soil_moisture])
    elif device_name=='SGP30':
        #retrieve values and insert record into database
        air_eco2=sensors.get_air_co2()
        air_tvoc=sensors.get_air_tvoc()
        
        database_use.write_to_db(table='gassensor_trans',
                                 write_info=[datetime.now(),
                                             plant_id,
                                             air_eco2,
                                             air_tvoc])
    elif device_name=='APDS9960':
        #retrieve values and insert record into database
        r,g,b,c=sensors.get_light_rgbc()
        
        database_use.write_to_db(table='lightsensor_trans',
                                 write_info=[datetime.now(),
                                             plant_id,
                                             r, g, b, c])
    elif device_name=='BME680':
        #retrieve values and insert record into database
        temp=sensors.get_air_temp()
        humidity=sensors.get_air_humidity()
        pressure=sensors.get_air_pressure()
        gasses=sensors.get_air_gas()
        
        database_use.write_to_db(table='airsensor_trans',
                                 write_info=[datetime.now(),
                                             plant_id,
                                             temp,
                                             humidity,
                                             gasses,
                                             pressure])
    elif device_name=='PiCamera':
        #Takes photo, stores to predefined location, writes info to database
        camera=PiCamera()
        
        fullpath=get_photos_path(plant_id, plant_name)
        
        camera.start_preview()
        time.sleep(5) #Important to allow camera to stabilize the image
        
        camera.capture(fullpath)
        camera.stop_preview()
        
        database_use.write_to_db(table='photo_trans',
                                 write_info=[datetime.now(),
                                             plant_id,
                                             fullpath])
        
    return    


def find_i2c_devices():
    #Called when main.py is initialized, then regularly
    #used to detect available I2C devices
    device_list=[]
    
    p = subprocess.Popen(['i2cdetect', '-y','1'],stdout=subprocess.PIPE,) 
    #cmdout = str(p.communicate())
    
    for i in range(0,9):
        line = str(p.stdout.readline())
        #print(line)
        
        #Parse line for addresses
        if i==0:
            pass #Header row; no useful information available
        else:
            line_list=line.split()
            for addr in line_list:
                try:
                    addr=int(addr)
                    device_list.append('0x'+str(addr))
                except:
                    pass
    
    return device_list

