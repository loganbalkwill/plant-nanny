import sys
sys.path.insert(0, '..')

import settings

def log_action(event,result, additional_info=''):
    #break apart event into components
    plant_id, plant_name, device_id, device_name, action_freq=event
    
    
    #create writing information
    if result=='success':
        severity='i' #informational
        message_prefix='Successfully performed device action(s): '
    elif result=='failure':
        severity='w' #warning
        message_prefix='failed to performe device action(s): '
        
    message_base= 'plant_id= %s, plant_name= %s, device_id= %s, device_name= %s' % (plant_id, plant_name, device_id, device_name)
    
    message=message_prefix + message_base
    
    if additional_info!='':
        message=message + '; ' + additional_info
            
    log_info(severity,message)
    
def log_info(log_level,message):
    
    return ''
