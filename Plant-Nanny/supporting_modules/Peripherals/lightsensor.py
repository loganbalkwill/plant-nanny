#!/usr/bin/env python
#Light Sensor Service

__status__ = "Production"

import adafruit_apds9960.apds9960 #APDS9960 light sensor
from board import SCL, SDA
import busio
import time
import datetime
import atexit
import sys

#Define I2C interface
i2c = busio.I2C(SCL, SDA, frequency=100000)

def begin_session( Assigned_id='', sleep_interval = 1, read_freq_mins=1, start_with_read=True ):
    #CALLED FROM THE APPLICATION
    #initialize device
    try:
        apds = adafruit_apds9960.apds9960.APDS9960(i2c)
        apds.enable_color=True
        send_health_info(assigned_id=Assigned_id , service=__file__ , result="Success" , msg="Light Sensor Service (APDS9960) has started")
    except:
        send_health_info(assigned_id=Assigned_id , service=__file__ , result="Failure" , msg="Light Sensor Service (APDS9960) could not be started")
        exit
    
    #begin 
    while True:
        r,g,b,c=apds.color_data
        print("Red: %s; Green: %s; Blue: %s; Clear: %s"%(r,g,b,c))
        time.sleep(sleep_interval)
        """database_use.write_to_db(table='lightsensor_trans',
                                 write_info=[datetime.now(),
                                 Assigned_id,
                                 r, g, b, c])"""

def testing_mode (sleep_interval = 1):
    try:
        apds = adafruit_apds9960.apds9960.APDS9960(i2c)
        apds.enable_color=True
    except:
        print("FAIL")
        exit
        
    while True:
        r,g,b,c = apds.color_data
        print("Red: %s; Green: %s; Blue: %s; Clear: %s"%(r,g,b,c))
        time.sleep(sleep_interval)

def pre_exit():
    #called before the program/process is terminated
    #TODO log that the process was exited properly
    print("Pre-Exit Routine")
    
def exceptionHandler(exctype, val, tb):
    #TODO logging this info
    #TODO log that the process is no longer running
    print('Unhandled Exception!')
    print('    Exception Type: %s', exctype)
    print('    Value: %s', val)
    print('    Traceback: %s', tb)


def send_health_info(assigned_id,service,result, msg):
    #DUMMY FUNCTION
    #TODO create actual function (in logger?)
    print(msg)

atexit.register(pre_exit)

if __name__=='__main__':
    
    if __status__=='Testing':
        try:
            print("Beginning Light Sensor Service (Test Mode)")
            testing_mode()
        except:
            #Error encountered during operation
            print("ERROR")
    elif __status__=='Production':
        print("Beginning Light Sensor Service")
        begin_session()
        
