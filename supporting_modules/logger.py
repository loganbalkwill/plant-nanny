from datetime import datetime
import os, sys
sys.path.insert(0, '..')

import settings
import supporting_modules.database_use as db

def log_action(event,result, additional_info=''):
    #break apart event into components
    plant_id, plant_name, device_id, device_name, action_freq=event
    
    
    #create writing information
    if result=='success':
        severity='d' #informational
        message_prefix='Successfully performed device action(s): '
    elif result=='failure':
        severity='w' #warning
        message_prefix='Failed to perform device action(s): '
        
    message_base= 'plant_id= %s, plant_name= %s, device_id= %s, device_name= %s' % (plant_id, plant_name, device_id, device_name)
    
    message=message_prefix + message_base
    
    if additional_info!='':
        message=message + '; ' + additional_info
            
    log_info(severity,message)
    
    
def log_info(log_level,message):
    
    if log_level=='p':
        dt=datetime.now()
        print('(' + dt.strftime("%m/%d/%Y, %H:%M:%S") + '): ' + message)
    elif log_level in settings.log_levels:
        db.write_to_db(table='log_trans',
                                 write_info=[datetime.now(), log_level, message])


def log_locally(info, filename, folder_path=settings.log_directory, filetype=settings.file_suffix):
    #called when database is unavailable
    
    fullpath=folder_path + filename + filetype
    
    #Make directory if doesnt already exist
    if os.path.exists(folder_path)==False:
        os.mkdir(folder_path)
    
    #Write information to file
    f=open(fullpath,"a")
    f.write(str(info) + '\n')
    f.close()

def local_logs_exist():
    #checks if any queue exists for uploading data to database
    directory=settings.log_directory
    
    count=0
    logfiles=0
    otherfiles=0
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt") or filename.endswith(".csv"):
            logfiles+=1
            f=open(directory+filename,"r")
            for line in f:
                count+= 1
        else:
            otherfile+=1
            
    if otherfiles!=0:
        msg="%s log(s) exist between %s log file(s) (%s non-log files exist)" % (count, logfiles, otherfiles)
    else:
        msg="%s log(s) exist between %s log file(s)" % (count, logfiles)
        
        
    return count, msg



if __name__=="__main__":
    local_logs_exist()