#!/usr/bin/env python

"""main.py:    
               -hosts main project code
               -hosts list and notes for unfinished project sections
"""

__author__    = "Logan Balkwill"
__date__      = "September 10, 2020"
__version__   = "1.0.1"
__maintainer__= "Logan Balkwill"
__email__     = "lgb0020@gmail.com"


import time
import math
import settings as s
import supporting_functions as funk
import soilsensor
import database_use as db

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
"""



#########################
### STARTUP PROCEDURE ###
#########################

#Check Peripherals
    #Build list of available sensors
sensors=db.get_sensor_list(additional_sql="active=1")
sensor_freq=db.get_sensor_frequencies(additional_sql="active=1")

#Check Database Connection
    #Check for queued logs

#Check Emailing Functionality

#Calculate looping frequency
loop_freq=funk.get_loop_frequency(sensor_freq)


#########################
####### MAIN LOOP #######
#########################
def main():
    while 1==1:
        
        #Check sensors
        for s in sensors:
            #Check if check interval has elapsed
                #Yes
                #Record sensor value
                #Reset interval counter
            
            #Increment interval counter
            break
        
        time.sleep(60*loop_freq)
        

if __name__=='__main__':
    main()
