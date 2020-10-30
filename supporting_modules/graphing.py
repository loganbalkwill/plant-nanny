import sys
sys.path.insert(0, '..')

import datetime as dt
import supporting_modules.database_use as db

def get_airtemp_data(plantid, input_date=str(dt.date.today())):
    #returns datasets for airtemp data for a given date, plant_id
    
    SQL_base="SELECT a.DateTime, a.AirTemp_DegC FROM airsensor_trans a WHERE a.DateTime >= '%s' AND a.DateTime < '%s' AND a.plant_id= '%s'"

    #validate date input
    try:
        date1=dt.date.fromisoformat(input_date)
    except:
        raise Exception("Date value '%s' supplied is not in a recognizable date format" % input_date)
    
    date2 = date1 + dt.timedelta(days=1)
    SQL_complete= (SQL_base % (date1, date2, plantid))
    
    
    data=db.retrieve_data(sql_query=SQL_complete)
    
    print(data)
    
if __name__=='__main__':
    get_airtemp_data(plantid=2)