#!/usr/bin/env python

"""main.py:    
               -hosts main project code
               -hosts list and notes for unfinished project sections
"""

__author__    = "Logan Balkwill"
__date__      = "September 10, 2020"
__version__   = "2.0.0"
__maintainer__= "Logan Balkwill"
__email__     = "lgb0020@gmail.com"

__status__    = "TESTING"

import time
import math
import settings as s
import multiprocessing
import supporting_modules.logger as logging
import supporting_modules.actions as actions
import supporting_modules.device_info as device_info
import supporting_modules.database_use as db

"""
GENERAL ALGORITHM:
    
    STARTUP:
        -CHECK AVAILABLE PERIPHERALS
        -CHECK DATABASE CONNECTION
            -UPLOAD QUEUED LOGS (IF EXISTS)
        -CHECK EMAILING FUNCTIONALITY
        -CALCULATE SLEEP FREQUENCY BETWEEN LOOPS
        
    MAIN LOOP:
        -READ REQUIRED INSTRUMENTS
        -WRITE ^ TO DATABASE
        -CHECK VALUE AGAINST ALLOWABLE CONSTRAINTS
        -PERFORM ACTION(S) AS REQUIRED:
            -PERFORM PHYSICAL ACTION (I.E. WATER)
            -NOTIFY SUBSCRIBER(S) VIA EMAIL

-----------------------------------------------------------------

VERSIONING:
    1.0.1                   -   I AM BORN
    1.1.1                   -   Major code restructuring (no significant program impact)
    1.2.1   (2020-12-18)    -   Patches to fit new db structure
    
    2.0.0   (2021-01-24)    -   MAJOR CODE OVERHAUL
                                -   Threading sensor scripts (TODO) 
                                -   Use standard "logging" python library; depricate "logger" (TODO)
                                -   Script to start program on launch (TODO: register script in crontab) 
"""

#########################
### STARTUP PROCEDURE ###
#########################
#Initialize Global Variables
i2c_available=[]
plant_devices_list=[]
action_freq_list=[]

def startup():
    #Acknowledge global variables
    global i2c_available, plant_devices_list, action_freq_list
    
    #Check Peripherals
    #Build list of sensors in-use
    i2c_available=device_info.find_i2c_devices()
    plant_devices_list=db.build_plant_devices_list()

    ###############################
    #   START DEVICE SERVICES
    ###############################
    

    ###############################
    #   START SUPPORTING SERVICES
    ###############################


#########################
####### MAIN LOOP #######
#########################
def main():
    while True:
        print("do something")
        
def map_service(action):
    #looks at action and starts the relevant process
    Assigned_id, Assigned_type, Assigned_name, device_id, device_name, action_freq =action

    if device_id==3:        #STEMMA Soil Sensor
        script_name='soilsensor.py'
    elif device_id==2:       #SGP30
        script_name='gassensor.py'
    elif device_id==6:        #APDS9960
        script_name='lightsensor.py'
    elif device_id==1:         #BME680
        script_name='airsensor.py'
    elif device_id==5:      #PiCamera
        script_name='camera.py'
    else:
        raise Exception('Device not defined! please address in main.py')
    
    return script_name


if __name__=='__main__':
    startup()
    main()
