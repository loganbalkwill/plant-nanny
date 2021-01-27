#Light Sensor Service
import adafruit_apds9960.apds9960 #APDS9960 light sensor
from board import SCL, SDA
import busio
import time
import atexit
import sys

#Define I2C interface
i2c = busio.I2C(SCL, SDA, frequency=100000)

def begin_session(sleep_interval = 10):
    #CALLED FROM THE APPLICATION
    

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

sys.excepthook=exceptionHandler
atexit.register(pre_exit)

if __name__=='__main__':
    #Assume it's being called in TESTING mode
    try:
        print("Beginning Sensor Test Mode")
        testing_mode()
    except:
        #Error encountered during operation
        print("ERROR")