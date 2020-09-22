import sys
import time
from board import SCL, SDA
import busio

sys.path.insert(0, '..')

import settings
import adafruit_sgp30  #SGP30 Air Gas Sensor 
from adafruit_seesaw.seesaw import Seesaw #STEMMA Soil Sensor
import adafruit_apds9960.apds9960 #APDS9960 light sensor
import adafruit_bme680 #BME680 Air Condition Sensor


#Initialize the I2C interface
i2c = busio.I2C(SCL, SDA, frequency=100000)
 
# Create sensor objects existing on the I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
ss = Seesaw(i2c, addr=settings.addr_sensor_soil)
apds = adafruit_apds9960.apds9960.APDS9960(i2c)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

#Initiate sensor objects (if required)
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

apds.enable_color=True

elapsed_sec = 0

#SENSOR FUNCTIONS

def get_soil_moisture():
    #retrieve latest soil moisture value
    return ss.moisture_read()

def get_soil_temp():
    #retrieve latest soil temperature value (Degrees Celcius)
    return ss.get_temp()

def get_air_co2():
    #retrieve latest air eCO2 reading
    return sgp30.eCO2

def get_air_tvoc():
    #retrieve latest air TVOC reading
    return sgp30.TVOC

def get_air_temp():
    #retrieve latest air temperature reading (Degrees C)
    return bme680.temperature

def get_air_humidity():
    #retrieve latest air humidity reading (%)
    return bme680.humidity

def get_air_pressure():
    #retrieve latest air pressure reading (hPa)
    return bme680.pressure

def get_air_gas():
    #retrieve latest air gas reading (ohms; proportional to TVOC reading)
    return bme680.gas


def get_light_rgbc():
    #retrieves latest lighting conditions
    r,g,b,c= apds.color_data
    return (r,g,b,c)


if __name__=='__main__':
    
    print(get_light_rgbc())
    while True:
        print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
        time.sleep(1)
        elapsed_sec += 1
        if elapsed_sec > 10:
            elapsed_sec = 0
            print(
                "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
                % (sgp30.baseline_eCO2, sgp30.baseline_TVOC)
            )
