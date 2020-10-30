import sys
sys.path.insert(0, '..')

import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import supporting_modules.database_use as db

def airtemp_graph(plant_id, target_date=str(dt.date.today())):
    times, temps = get_airtemp_data(plantid=plant_id, input_date=target_date)
    plt.plot(times, temps)
    plt.ylabel('Degrees Celcius')
    plt.xlabel(target_date)
    plt.xlim(0,24)
    plt.suptitle('Air Temperature')
    plt.show()
    
def get_airtemp_data(plantid, input_date=str(dt.date.today())):
    #returns datasets for airtemp data for a given date, plant_id
    
    SQL_base="SELECT CAST(a.DateTime as Time) as Timestamp, a.AirTemp_DegC FROM airsensor_trans a WHERE a.DateTime >= '%s' AND a.DateTime < '%s' AND a.plant_id= '%s'"

    #validate date input
    try:
        date1=dt.date.fromisoformat(input_date)
    except:
        raise Exception("Date value '%s' supplied is not in a recognizable date format" % input_date)
    
    #build query parameters
    date2 = date1 + dt.timedelta(days=1)
    SQL_complete= (SQL_base % (date1, date2, plantid))
    
    #run query
    data = db.retrieve_data(sql_query=SQL_complete)

    #unpack data
    times=[]
    airtemp=[]
    
    for i in data:
        times.append(i[0].seconds/3600)
        airtemp.append(i[1])
    
    return times, airtemp
    
if __name__=='__main__':
    #t, a = get_airtemp_data(plantid=2)
    
    airtemp_graph(plant_id=2)