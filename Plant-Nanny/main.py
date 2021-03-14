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
import supporting_modules.dictionaries as dictionaries

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
                                -   Emailer & Graphing support
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
    
    #Check that project is set up

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


#I might move this class to another file
class device():
    RoomID=''
    RoomName=''

    PlantID=''
    PlantName=''

    DeviceID=''
    DeviceName=''

    ActionFrequency_mins=10
    ScriptName=''

    def __init__(self, key_ID):
        self.keyID=key_ID
        self.unpack_keyID(self.keyID)
        self.get_info()

    def unpack_keyID(self, keyID):
        #unpacks the keyID string to identify basic information
        #keyID is supplied in the format "<RoomID>|<PlantID>|<DeviceID>"
        x=keyID.split('|')
        
        if len(x)!=3:
            raise Exception("Could not unpack keyID due to mismatch in key length; Expected: 3 , Supplied: %s" %len(x))

        self.RoomID=x[0]
        self.PlantID=x[1]
        self.DeviceID=x[2]

    def get_info(self):
        #gathers additional information about the device assignment using database queries
        
        #import SQL Query Dictionary
        sql_dict=dictionaries.sql_select.copy()

        self.RoomName=db.query_db(sql_dict['room_name'], self.RoomID)
        self.PlantName=db.query_db(sql_dict['plant_name'], self.PlantID)
        self.DeviceName=db.query_db(sql_dict['device_name'], self.DeviceID)
        self.ActionFrequency_mins=db.query_db(sql_dict['action_frequency'], self.keyID)
        self.ScriptName=db.query_db(sql_dict['script_name'], self.DeviceID)


if __name__=='__main__':
    startup()
    main()
