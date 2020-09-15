import math

def get_loop_frequency(numlist):
    #returns the frequency of looping in the main procedure
    
    #default returns 1 minute
    GCD=1
    reclist=[]
    #if any of the numbers provided are less than 1 minute (non-negative),
    #a greatest common divisor (GCD) is calculated
    
    for record in numlist:
        for num in record:
            if num<0: 
                print("ERROR: negative number provided for loop frequency; please correct")
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