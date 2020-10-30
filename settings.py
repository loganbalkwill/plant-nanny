#settings.py


#MySQL Database Information:

database_name='plantnanny'
host='localhost'
username='mainuser'
password='mainuser'

phpmyadmin_password='Balk45610'

#Interval for checking for new information
refresh_mins=10

#Local Logging Information:
#(only used to store data if MySQL database is unavailable)
log_directory='/home/pi/Documents/Plant_Nanny/Logs/'
file_suffix='.txt'

#Log levels permitted; comment out any undesired level
log_levels=(
    'i', #informational
    'w', #warning
    #'d', #debugging
    's', #severe
    #'p', #print (prints to the shell; not logged into database) DO NOT UNCOMMENT!!!
    )
    
#Instrument Settings
read_frequency_mins=1

#I2C Instruments

addr_sensor_soil=0X36
addr_sensor_gas=0X58


#Camera Information
image_directory='/home/pi/Documents/Plant_Nanny/Plant-Photos/'
image_filetype='.jpg'


#Graphics Information
graphics_directory='/home/pi/Documents/Plant_Nanny/Charts/'
graphics_filetype='.png'
