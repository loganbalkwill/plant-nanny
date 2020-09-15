import math
import time
from datetime import datetime
import settings
import database_use
import soilsensor

def get_loop_frequency(numlist):
    #returns the frequency of looping in the main procedure
    
    #default returns 1 minute
    GCD=settings.read_frequency_mins
    reclist=[]
    #if any of the numbers provided are less than 1 minute (non-negative),
    #a greatest common divisor (GCD) is calculated
    
    for num in numlist:
        if num<0: 
            print("ERROR: negative number provided for loop frequency; please correct")
            #This shouldn't happen because of the database table settings
            break
        elif num>1 and num!=math.ceil(num):
            print("WARNING: partial minute provided for loop frequency (%s mins); number will be rounded to %s mins for calculation" % (num, math.floor(num)))
            
            num=math.floor(num)
        reclist.append(num)
    
    num_min=min(reclist)
    if num_min<1 and num_min>0:
        #need to calculate new GCM
        GCD=(math.gcd(math.floor(num_min*60),60))/60
    
    return GCD        

def get_action_freqs(plant_device_list):
    #returns list of action frequencies from main list
    
    #input list in the form of:
    #PlantID, Plant Name, Device_ID, Device Name, Action_Frequency_Min
    
    freq_list=[]
    
    for rw in plant_device_list:
        plant_id, plant_name, device_id, device_name, action_freq=rw
        freq_list.append(action_freq)
            
    
    return freq_list

def condition_frequency(num):
    #return suitable frequency
    
    if num>1 and num!=math.ceil(num):    
        num=math.floor(num)
    return num
    
def perform_action(action):
    #called by main loop when specified frequency has elapsed
    
    #input supplied as list in form:
    #PlantID, Plant Name, Device_ID, Device Name, Action_Frequency_Min
    
    plant_id, plant_name, device_id, device_name, action_freq, =action
    
    #decide what action to perform
    if device_name=='STEMMA Soil Sensor':
        #retrieve values and insert record into database
        soil_temp=soilsensor.get_temp()
        soil_moisture=soilsensor.get_moisure()
        
        database_use.write_to_db(table='soilsensor_trans',write_info=[datetime.now(),plant_id,soil_temp,soil_moisture])

    return
