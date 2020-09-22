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
    
    if log_level in settings.log_levels:
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
    f.write(info)
    f.close()
