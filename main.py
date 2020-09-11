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
    sensors=db.get_sensors()

#Check Database Connection
    #Check for queued logs

#Check Emailing Functionality

#Calculate looping frequency
loop_freq=get_loop_frequency(sensors)

#########################
####### MAIN LOOP #######
#########################

def main():
    while true:
        
        #Check sensors
        for s in sensors:
            #Check if check interval has elapsed
                #Yes
                #Record sensor value
                #Reset interval counter
            
            #Increment interval counter
            break
        
        time.sleep(60*loop_freq)
        
def get_loop_frequency(numlist):
    #returns the frequency of looping in the main procedure
    
    #default returns 1 minute
    GCD=1
    
    #if any of the numbers provided are less than 1 minute (non-negative),
    #a greatest common divisor (GCD) is calculated
    
    for num in numlist:
        if num<0: 
            print("ERROR: negative number provided for loop frequency; please correct")
            break
        elif num>1 and num!=math.ceil(num):
            print("WARNING: partial minute provided for loop frequency (%s mins); number will be rounded to %s mins for calculation" % (num, math.floor(num)))
            
            num=math.floor(num)
        
    if min(numlist)<1 and min(numlist)>0:
        #need to calculate new GCM
        GCD=(math.gcd(math.floor(num*60),60))
    
    return GCD

        
if __name__=='__main__':
    main()
